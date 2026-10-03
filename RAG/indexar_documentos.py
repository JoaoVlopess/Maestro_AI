from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from RAG.banco_vetorial import obter_banco_vetorial
from tools.extracao_textual_pdf import extrair_texto_pdf


def criar_documento(caminho_arquivo: str) -> Document:
    """
    Cria um objeto Document a partir de um arquivo PDF.

    Args:
        caminho_arquivo (str): O caminho para o arquivo PDF.

    Returns:
        Document: Um objeto Document contendo o conteúdo do PDF.
    """
    texto = extrair_texto_pdf(caminho_arquivo)
    return Document(page_content=texto, metadata={"source": caminho_arquivo})


def dividir_documento(documento: Document, tamanho_chunk: int = 1000, sobreposicao_chunk: int = 200) -> list[Document]:
    """
    Divide um objeto Document em chunks menores.

    Args:
        documento (Document): O objeto Document a ser dividido.
        tamanho_chunk (int): O tamanho máximo de cada chunk.
        sobreposicao_chunk (int): A quantidade de sobreposição entre chunks.

    Returns:
        list[Document]: Uma lista de objetos Document representando os chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=tamanho_chunk,
        chunk_overlap=sobreposicao_chunk,
        length_function=len
    )
    return text_splitter.split_documents([documento])


def indexar_chunks(chunks: list[Document]) -> None:
    """Adiciona os chunks à coleção configurada no banco vetorial."""
    banco = obter_banco_vetorial()
    banco.add_documents(chunks)


caminhos_pdf = [
    "apostilas_pdf/apostila_1.pdf",
]

def main():
    documento = criar_documento(caminhos_pdf[1])
    chunks = dividir_documento(documento)
    indexar_chunks(chunks)

    print(f"Indexação concluída: {len(chunks)} chunks.")


if __name__ == "__main__":
    main()
