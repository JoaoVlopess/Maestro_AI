import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from models.maestro import SolicitacaoAula, RespostaMaestro
from prompts.prompt_maestro import PROMPT_MAESTRO


load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError(
        "A variável GOOGLE_API_KEY não foi encontrada no arquivo .env"
    )

modelo = ChatGoogleGenerativeAI (
    model="gemini-3.5-flash-lite"
)

maestro_estruturado = modelo.with_structured_output(RespostaMaestro)

def gerar_aula(solicitacao: SolicitacaoAula) -> RespostaMaestro:
    mensagem_usuario = (
        "human",
        f"""
        Pergunta: {solicitacao.pergunta}
        Nível do aluno: {solicitacao.nivel_aluno}
        Instrumento escolhido: {solicitacao.instrumento_escolhido}
        """,
    )

    mensagens = [
        PROMPT_MAESTRO,
        mensagem_usuario,
    ]

    resposta = maestro_estruturado.invoke(mensagens)

    return resposta
