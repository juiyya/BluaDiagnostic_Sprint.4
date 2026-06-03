from langchain_core.messages import SystemMessage, AIMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from utils.helpers import carregar_prompt
from observability.logger import logger

class RoteamentoSupervisor(BaseModel):
    destino: str = Field(
        description="Obrigatório. Valores permitidos: 'schedule_agent', 'triage_agent', 'prescription_agent', 'escalation_agent'."
    )
    justificativa: str = Field(
        description="Breve explicação do porquê escolheu essa rota."
    )

def supervisor_node(state):
    logger.info("Supervisor acionado.")
    prompt_text = carregar_prompt("supervisor_prompt.md")
    
    llm = ChatOllama(model="qwen2.5:14b", temperature=0)
    llm_estruturado = llm.with_structured_output(RoteamentoSupervisor)
    
    mensagens = [SystemMessage(content=prompt_text)] + state["messages"]
    
    try:
        decisao = llm_estruturado.invoke(mensagens)
        rota = decisao.destino
        logger.info(f"[Supervisor] Decidiu: {rota} | Motivo: {decisao.justificativa}")
    except Exception as e:
        logger.error(f"Erro de formatação do Llama. Fallback ativado. Erro: {e}")
        rota = "triage_agent"
        
    return {"messages": [AIMessage(content=rota, name="supervisor")]}