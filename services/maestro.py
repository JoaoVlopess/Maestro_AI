import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from models.maestro import SolicitacaoAula, RespostaMaestro
from prompts.prompt_maestro import PROMPT_MAESTRO
from tools.ferramentas_maestro import calcular_intervalo
from langchain.agents.structured_output import ProviderStrategy

load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError(
        "A variável GOOGLE_API_KEY não foi encontrada no arquivo .env"
    )

modelo = ChatGoogleGenerativeAI (
    model="gemini-3.5-flash-lite"
)

agente_maestro = create_agent(
    model=modelo,
    tools=[calcular_intervalo],
    system_prompt=PROMPT_MAESTRO,
    response_format=ProviderStrategy(RespostaMaestro),
)

def gerar_aula(solicitacao: SolicitacaoAula) -> RespostaMaestro:
    mensagem_usuario = f"""
    Pergunta: {solicitacao.pergunta}
    Nível do aluno: {solicitacao.nivel_aluno}
    Instrumento escolhido: {solicitacao.instrumento_escolhido}
    """

    resultado = agente_maestro.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": mensagem_usuario,
                }
            ]
        }
    )

    for mensagem in resultado["messages"]:
        mensagem.pretty_print()
    return resultado["structured_response"]