from langchain_core.documents import Document

from RAG.banco_vetorial import obter_banco_vetorial


def buscar_documentos(
    pergunta: str,
    quantidade: int = 3,
) -> list[Document]:
    """Busca no Chroma os chunks mais relacionados à pergunta."""
    banco = obter_banco_vetorial()

    documentos = banco.similarity_search(
        query=pergunta,
        k=quantidade,
    )

    return documentos


def main() -> None:
    pergunta = "O que é andamento musical?"
    documentos = buscar_documentos(pergunta)

    print(f"Pergunta: {pergunta}")
    print(f"Documentos encontrados: {len(documentos)}")

    for numero, documento in enumerate(documentos, start=1):
        print(f"\n--- Resultado {numero} ---")
        print(f"Fonte: {documento.metadata.get('source', 'Fonte não informada')}")
        print(documento.page_content)


if __name__ == "__main__":
    main()
