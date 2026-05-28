from langgraph.graph import END
from observability.logger import logger

def roteamento_supervisor(state):
    destino = state["messages"][-1].content
    rotas_validas = ["schedule_agent", "triage_agent", "prescription_agent", "escalation_agent"]
    
    if destino in rotas_validas:
        return destino
        
    logger.warning(f"Rota inválida capturada: {destino}. Encerrando.")
    return END