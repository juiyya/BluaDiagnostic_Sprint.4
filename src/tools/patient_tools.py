import json
import os
from langchain_core.tools import tool
from observability.logger import logger

def carregar_banco_pacientes():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, "..", "..", "data", "pacientes_mock.json")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Arquivo de banco de dados mockado não encontrado em: {filepath}")
        return {}

@tool
def buscar_dados_wearable(patient_id: str) -> str:
    """
    Busca e retorna os dados de telemetria e sinais vitais (frequência cardíaca, SpO2) do dispositivo wearable do paciente.
    
    REGRAS OBRIGATÓRIAS:
    1. O parâmetro 'patient_id' é ESTRICTAMENTE OBRIGATÓRIO.
    2. NUNCA invente ou adivinhe um ID. Se o ID não foi fornecido na conversa, NÃO CHAME ESTA FERRAMENTA. Volte e pergunte ao usuário.
    """
    logger.info(f"[Tool] buscar_dados_wearable acionada para o ID: {patient_id}")
    return f"Dados de telemetria do Wearable para o paciente {patient_id}: Frequência Cardíaca em repouso 110 bpm. Saturação de Oxigênio (SpO2): 98%."

@tool
def buscar_historico_paciente(patient_id: str) -> str:
    """
    Busca e retorna o prontuário e histórico médico completo do paciente (alergias, medicações de uso contínuo, consultas anteriores).
    
    REGRAS OBRIGATÓRIAS:
    1. O parâmetro 'patient_id' é ESTRICTAMENTE OBRIGATÓRIO.
    2. NUNCA invente ou adivinhe um ID. Se o ID não foi fornecido na conversa, NÃO CHAME ESTA FERRAMENTA. Volte e pergunte ao usuário.
    """
    logger.info(f"[Tool] buscar_historico_paciente acionada para o ID: {patient_id}")
    db = carregar_banco_pacientes()
    p = db.get(str(patient_id))
    if p:
        logger.info(f"Prontuário do paciente {patient_id} ({p['nome']}) recuperado com sucesso.")
        return f"Paciente {p['nome']}, {p['idade']} anos, histórico de {p['historico']}, última consulta em {p['ultima_consulta']}, uso contínuo de {p['uso_continuo']}. Alergias: {p['alergias']}."
    
    logger.warning(f"[Tool]Tentativa de busca falhou: Paciente ID {patient_id} não localizado no banco local.")
    return f"Paciente com o identificador {patient_id} não foi encontrado no sistema da Care Plus."