from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from utils.helpers import carregar_prompt
from tools.patient_tools import buscar_historico_paciente
from tools.scheduling_tools import agendar_teleconsulta 
from observability.logger import logger

scheduling_tools = [buscar_historico_paciente, agendar_teleconsulta]

def schedule_node(state):
    logger.info("Schedule Agent acionado.")
    prompt_text = carregar_prompt("schedule_prompt.md")
    llm = ChatOllama(model="qwen2.5:14b", temperature=0)

    msgs_validas = [
        msg for msg in state["messages"] 
        if getattr(msg, 'name', '') != "supervisor"
    ]

    if len(msgs_validas) <= 2:
        logger.info("Início de fluxo: Ferramentas de agendamento bloqueadas para coleta de ID.")
        prompt_text += "\n\n[SISTEMA: ESTA É A SUA PRIMEIRA INTERAÇÃO. SOLICITE O ID DO PACIENTE. NÃO INVENTE DADOS.]"
    else:
        logger.info("Fluxo em andamento.")
        llm = llm.bind_tools(scheduling_tools)
    
    mensagens = [SystemMessage(content=prompt_text)] + msgs_validas
    resposta = llm.invoke(mensagens)
    
    return {"messages": [resposta]}