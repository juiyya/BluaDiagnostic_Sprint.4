from langchain_core.tools import tool
from observability.logger import logger

@tool
def agendar_teleconsulta(patient_id: str, data: str, horario: str, especialidade: str) -> str:
    """
    Use esta ferramenta para efetivar o agendamento de uma teleconsulta no sistema.
    
    REGRAS CRÍTICAS DE USO:
    1. Você NÃO PODE inventar, supor ou gerar um 'patient_id' falso. O usuário DEVE fornecer o ID explicitamente na conversa.
    2. Você DEVE ter coletado a 'data', o 'horario' e a 'especialidade' informados pelo usuário.
    3. Se faltar QUALQUER UM desses 4 parâmetros, NÃO CHAME ESTA FERRAMENTA. Volte e pergunte ao usuário a informação que falta.
    """
    logger.info(f"[Tool] agendar_teleconsulta acionada para o paciente {patient_id} em {data} às {horario} ({especialidade}).")
    
    return f"Agendamento realizado com sucesso para o paciente {patient_id} com o especialista em {especialidade} no dia {data} às {horario}."