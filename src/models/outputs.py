from pydantic import BaseModel, Field
from typing import Literal

class RoteamentoSupervisor(BaseModel):

    proximo_agente: Literal["TRIAGEM", "PRESCRIÇÃO", "ESCALONAMENTO", "AGENDAMENTO"]
    justificativa: str = Field(description="Breve motivo clínico da escolha do agente.")