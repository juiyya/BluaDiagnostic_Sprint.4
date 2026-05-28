from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from utils.helpers import carregar_prompt
from tools.patient_tools import buscar_historico_paciente, buscar_dados_wearable
from observability.logger import logger

triage_tools = [buscar_historico_paciente, buscar_dados_wearable]

def triage_node(state):
    logger.info("Triage Agent acionado.")
    prompt_text = carregar_prompt("triage_prompt.md")
    llm = ChatOllama(model="qwen2.5:14b", temperature=0)
    
    msgs_validas = [
        msg for msg in state["messages"] 
        if getattr(msg, 'name', '') != "supervisor"
    ]
    
    if len(msgs_validas) <= 2:
        logger.info("Início de fluxo: Ferramentas de triagem bloqueadas.")
        prompt_text += "\n\n[SISTEMA: ESTA É A SUA PRIMEIRA INTERAÇÃO. FAÇA UMA PERGUNTA DE TRIAGEM PARA ENTENDER MELHOR OS SINTOMAS OU PEÇA O ID DO PACIENTE. NÃO INVENTE DADOS.]"
    else:
        logger.info("Fluxo em andamento: Ferramentas liberadas.")
        llm = llm.bind_tools(triage_tools)
    
    mensagens = [SystemMessage(content=prompt_text)] + msgs_validas
    resposta = llm.invoke(mensagens)
    
    return {"messages": [resposta]}