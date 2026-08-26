from typing import Literal

from pydantic import BaseModel


Instrumento = Literal["guitarra", "violao", "teclado", "baixo"]
NivelAluno = Literal["iniciante", "intermediario", "avancado"]
Dificuldade = Literal["facil", "medio", "dificil"]


class SolicitacaoAula(BaseModel):
    pergunta: str
    nivel_aluno: NivelAluno
    instrumento_escolhido: Instrumento = "teclado"


class RespostaMaestro(BaseModel):
    assunto_musical: str
    explicacao: str
    exemplo_aplicado_instrumento: str
    dificuldade: Dificuldade