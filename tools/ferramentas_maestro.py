from typing import Literal

from langchain.tools import tool

from tools.musica import obter_nota_por_intervalo
TipoIntervalo = Literal[
    "segunda menor",
    "segunda maior",
    "terça menor",
    "terça maior",
    "quarta justa",
    "quarta aumentada",
    "quinta diminuta",
    "quinta justa",
    "sexta menor",
    "sexta maior",
    "sétima menor",
    "sétima maior",
    "oitava justa",
]


# @tool
# def calcular_transposicao(nota_inicial: str, semitons: int) -> str:
#     """
#     Tool Calcula a nota resultante após transpor uma nota inicial
#     por determinada quantidade de semitons.
#     """
#     return transpor_nota(nota_inicial, semitons)

@tool
def calcular_intervalo(nota_inicial: str, intervalo: str):
    """
    Tool que Calcula a nota resultante após aplicar um determinado
    intervalo na nota em questão.
    OBS: SEMPRE escreva o nome do intervalo com letra minuscula e por extenso
    ex: segunda menor, terça maior, ...
    """
    return obter_nota_por_intervalo(nota_inicial,intervalo)