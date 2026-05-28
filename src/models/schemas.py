from pydantic import BaseModel, Field
from typing import List, Optional

class PacienteSchema(BaseModel):
    id: str
    nome: str
    idade: int
    historico: str
    uso_continuo: List[str]
    alergias: List[str]

class SinaisVitaisSchema(BaseModel):
    patient_id: str
    bpm: int
    spo2: int