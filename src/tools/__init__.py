from .patient_tools import buscar_historico_paciente, buscar_dados_wearable
from .scheduling_tools import agendar_teleconsulta
from .prescription_tools import buscar_diretrizes_careplus, checar_interacao_medicamentosa
from .emergency_tools import notificar_equipe_medica

all_tools = [
    buscar_historico_paciente,
    buscar_dados_wearable,
    agendar_teleconsulta,
    buscar_diretrizes_careplus,
    checar_interacao_medicamentosa,
    notificar_equipe_medica
]