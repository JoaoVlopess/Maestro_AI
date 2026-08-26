import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from Prompts.prompt_maestro import PROMPT_MAESTRO


COMANDO_HUMANO = (    
        "human",
        "Explique o que é um intervalo musical e dê um exemplo na guitarra.",
    )


load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError(
        "A variável GOOGLE_API_KEY não foi encontrada no arquivo .env"
    )

modelo = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.2,
)

mensagens = [PROMPT_MAESTRO, COMANDO_HUMANO]

resposta = modelo.invoke(mensagens)
print("\nMAESTRO AI\n")
print(resposta.text)