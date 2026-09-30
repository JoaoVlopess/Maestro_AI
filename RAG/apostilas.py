import os

from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from apostilas.extracao.apostila_teoria_musical import (
    APOSTILA_INTRODUCAO_TEORIA_MUSICAL,
)

load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError(
        "A variável GOOGLE_API_KEY não foi encontrada no arquivo .env"
    )

documentos = []

apostila_introducao_teoria_musical = Document(
    page_content=APOSTILA_INTRODUCAO_TEORIA_MUSICAL,
    metadata={"autor": "Opus 3", "source": "https://aprendamusica.opus3ensinomusical.com.br/wp-content/uploads/2024/07/Apostila-Teoria-Musical-Para-Iniciantes.docx-1.pdf"}
)
documentos.append(apostila_introducao_teoria_musical)


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)

chunks = text_splitter.split_documents(documentos)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
)

db = Chroma.from_documents(documents = chunks, embedding = embeddings, persist_directory = "db")