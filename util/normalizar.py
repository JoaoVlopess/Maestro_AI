import unicodedata


def normalizar_texto(texto: str) -> str:
    texto = texto.strip().lower()

    return "".join(
        caractere
        for caractere in unicodedata.normalize("NFD", texto)
        if unicodedata.category(caractere) != "Mn"
    )