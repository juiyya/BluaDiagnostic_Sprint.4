from langchain_core.messages import SystemMessage
from langchain_ollama import ChatOllama
from utils.helpers import carregar_prompt
from tools.emergency_tools import notificar_equipe_medica
from observability.logger import logger

escalation_tools = [notificar_equipe_medica]

def escalation_node(state):
    logger.info("Escalation Agent acionado.")
    prompt_text = carregar_prompt("escalation_prompt.md") 
    
    llm = ChatOllama(model="qwen2.5:14b", temperature=0).bind_tools(
        escalation_tools, tool_choice="notificar_equipe_medica")
    
    msgs_validas = [
        msg for msg in state["messages"] 
        if getattr(msg, 'name', '') != "supervisor"
    ]
    
    logger.info("Ferramentas de emergência liberadas.")
    
    mensagens = [SystemMessage(content=prompt_text)] + msgs_validas
    resposta = llm.invoke(mensagens)
    
    return {"messages": [resposta]}