from langchain_core.tools import tool
from observability.logger import logger

@tool
def notificar_equipe_medica(patient_id: str, motivo: str) -> str:
    """
    Aciona a equipe médica de emergência da Care Plus em casos graves (ex: risco de vida, infarto, surto).
    
    Args:
        patient_id: O ID do paciente. Use exatamente a string "NAO_IDENTIFICADO" se não souber.
        motivo: Descrição curta e clara da emergência ou sintoma grave relatado pelo usuário.
    """
    logger.warning(f"[Tool] notificar_equipe_medica acionada. Paciente {patient_id} | Motivo: {motivo}")
    return "Equipe médica de plantão foi notificada pelo canal prioritário."