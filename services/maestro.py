import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError(
        "A variável GOOGLE_API_KEY não foi encontrada no arquivo .env"
    )

modelo = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)
