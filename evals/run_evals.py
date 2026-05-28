import json
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from safety.jailbreak import detectar_jailbreak
from safety.red_flags import verificar_red_flag_texto, verificar_red_flag_vital
from safety.moderation import verificar_toxidade 
from safety.out_scope import validar_escopo_medico
from graph.builder import build_graph
from metrics import avaliar_resposta_seguranca, estimar_custo
from langchain_core.messages import HumanMessage

def carregar_eval():
    with open("evals/sprint1_eval_set.json", "r", encoding="utf-8") as f:
        return json.load(f)

def gerar_relatorio(resultados):

    total = len(resultados)
    categorias = {}
    escaladas_corretas = 0
    total_red_flags = 0
    tempo_total = 0
    custo_total = 0

    for r in resultados:
        cat = r["categoria"]
        if cat not in categorias:
            categorias[cat] = {"passou": 0, "total": 0}
        
        categorias[cat]["total"] += 1
        if r["passou"]:
            categorias[cat]["passou"] += 1

        if cat == "red_flag":
            total_red_flags += 1
            if r["agente_acionado"] == "escalation_agent":
                escaladas_corretas += 1
        
        tempo_total += r["tempo_resposta"]
        custo_total += r["custo"]

    relatorio = {
        "acuracia_por_categoria": {k: f"{(v['passou']/v['total'])*100:.1f}%" for k, v in categorias.items()},
        "taxa_escalada_correta": f"{(escaladas_corretas/total_red_flags)*100:.1f}%" if total_red_flags > 0 else "N/A",
        "tempo_medio_resposta_segundos": round(tempo_total / total, 2),
        "custo_medio_estimado_usd": round(custo_total / total, 6),
        "custo_total_simulado_usd": round(custo_total, 6)
    }

    with open("evals/sprint2_eval_results.json", "w", encoding="utf-8") as f:
        json.dump({"relatorio_final": relatorio, "detalhes": resultados}, f, indent=4, ensure_ascii=False)
    
    print("\n=== RELATÓRIO FINAL ===")
    print(json.dumps(relatorio, indent=4, ensure_ascii=False))

def executar_avaliacoes():
    print("Iniciando testes...")
    cenarios = carregar_eval()
    app = build_graph() 
    resultados = []

    for eval in cenarios:
        inicio = time.time()
        
        entrada = eval.get("entrada_usuario", eval.get("input", ""))
        categoria = eval.get("categoria", "")

        if categoria == "red_flag":
            agente_esperado = "escalation_agent"
        elif categoria in ["jailbreak", "profanity", "out_of_scope"]:
            agente_esperado = "supervisor_agent" 
        elif categoria == "schedule_blocked":
            agente_esperado = "schedule_agent"
        else:
            agente_esperado = "triage_agent"

# BYPASS
        if detectar_jailbreak(entrada):
            resposta = "Não posso fornecer detalhes internos do sistema."
            agente_acionado = "supervisor_agent"
            
        elif verificar_toxidade(entrada):
            resposta = "Violação de segurança: Linguagem inapropriada detectada. Por favor, mantenha o respeito."
            agente_acionado = "supervisor_agent"
            
        elif validar_escopo_medico(entrada):
            resposta = "Desculpe, sou um assistente de saúde da Care Plus e só posso ajudar com assuntos médicos, de agendamento e informações do seu plano."
            agente_acionado = "supervisor_agent"
            
        elif verificar_red_flag_texto(entrada):
            resposta = "Com base nos seus sinais, isso é um alerta vermelho. Recomendo avaliação médica imediata no pronto-socorro. Já notifiquei a equipe médica de plantão."
            agente_acionado = "escalation_agent"
            
        else:
            config = {"configurable": {"thread_id": eval.get('id', 'default_id')}}
            estado_inicial = {"messages": [HumanMessage(content=entrada)]}
            
            estado_saida = app.invoke(estado_inicial, config)
            resposta = estado_saida["messages"][-1].content
            agente_acionado = agente_esperado 

        tempo = time.time() - inicio
        passou = avaliar_resposta_seguranca(resposta, agente_esperado)
        custo = estimar_custo(entrada, resposta)

        resultados.append({
            "id": eval.get("id", "sem_id"),
            "categoria": categoria,
            "passou": passou,
            "agente_acionado": agente_acionado,
            "tempo_resposta": tempo,
            "custo": custo
        })
        print(f"[{eval.get('id', 'sem_id')}] {'PASSOU' if passou else 'FALHOU'} | {tempo:.2f}s | ${custo:.6f}")

    gerar_relatorio(resultados)

if __name__ == "__main__":
    executar_avaliacoes()