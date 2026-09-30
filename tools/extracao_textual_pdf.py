from pypdf import PdfReader

def extrair_texto_pdf(caminho_pdf):
    """
    Extrai o texto de um arquivo PDF.

    Args:
        caminho_pdf (str): O caminho para o arquivo PDF.

    Returns:
        str: O texto extraído do PDF.
    """
    reader = PdfReader(caminho_pdf)
    texto_extraido = ""

    for pagina in reader.pages:
        texto_extraido += pagina.extract_text()

    return texto_extraido
