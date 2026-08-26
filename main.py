import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.prompt_maestro import PROMPT_MAESTRO


from models.maestro import SolicitacaoAula


solicitacao = SolicitacaoAula(
    pergunta="O que é um intervalo musical?",
    nivel_aluno="iniciante",
    instrumento_escolhido="guitarra",
)

print(solicitacao)