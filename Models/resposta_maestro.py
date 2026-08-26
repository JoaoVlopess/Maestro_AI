from typing import Literal
from pydantic import BaseModel

class resposta_maestro(BaseModel):
    assunto_musical: str
    explicacao: str
    exemplo_aplicado_instrumento: str
    dificuldade: Literal["facil", "medio", "dificil"]
    instrumento_escolhido: str = "teclado"