from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from utils.helpers import carregar_prompt
from tools.prescription_tools import buscar_diretrizes_careplus, checar_interacao_medicamentosa
from tools.patient_tools import buscar_historico_paciente
from observability.logger import logger

prescription_tools = [buscar_diretrizes_careplus, checar_interacao_medicamentosa, buscar_historico_paciente]

def prescription_node(state):
    logger.info("Prescription Agent acionado.")
    prompt_text = carregar_prompt("prescription_prompt.md")
    llm = ChatOllama(model="qwen2.5:14b", temperature=0)
    
    msgs_validas = [
        msg for msg in state["messages"] 
        if getattr(msg, 'name', '') != "supervisor"
    ]
    
    if len(msgs_validas) <= 2:
        prompt_text += "\n\n[SISTEMA: ESTA É A SUA PRIMEIRA INTERAÇÃO. ENTENDA A DÚVIDA DO PACIENTE SOBRE MEDICAMENTOS ANTES DE BUSCAR DIRETRIZES OU INTERAÇÕES. NÃO INVENTE DADOS.]"
    else:
        logger.info("Fluxo em andamento.")
        llm = llm.bind_tools(prescription_tools)
    
    mensagens = [SystemMessage(content=prompt_text)] + msgs_validas
    resposta = llm.invoke(mensagens)
    
    return {"messages": [resposta]}