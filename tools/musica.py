from util.normalizar import normalizar_texto


NOTAS_CROMATICAS = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
INTERVALOS = {
    "uníssono": 0,
    "segunda menor": 1,
    "segunda maior": 2,
    "terça menor": 3,
    "terça maior": 4,
    "quarta justa": 5,
    "quarta aumentada": 6,
    "quinta diminuta": 6,
    "quinta justa": 7,
    "quinta aumentada": 8,
    "sexta menor": 8,
    "sexta maior": 9,
    "sétima menor": 10,
    "sétima maior": 11,
    "oitava justa": 12,
    "nona menor": 13,
    "nona maior": 14,
    "décima menor": 15,
    "décima maior": 16,
    "décima primeira justa": 17,
    "décima primeira aumentada": 18,
    "décima quinta justa": 24,
}

INTERVALOS_NORMALIZADOS = {
    normalizar_texto(nome): semitons
    for nome, semitons in INTERVALOS.items()
}


def transpor_nota(nota_inicial: str, semitons: int):
    """
    Tool para calcular a distancia de um intervalo sabendo a quesntidade de semitons e a nota de partida.
    """
    indice = NOTAS_CROMATICAS.index(nota_inicial)
    
    indice_nota_transposta = (indice + semitons) % len(NOTAS_CROMATICAS)
    
    nota_transposta = NOTAS_CROMATICAS[indice_nota_transposta]
    return nota_transposta

def obter_nota_por_intervalo(nota_inicial: str, intervalo: str):
    intervalo = intervalo.strip().lower()
    intervalo_normalizado = normalizar_texto(intervalo)


    if intervalo_normalizado not in INTERVALOS_NORMALIZADOS:
        raise ValueError(f"Intervalo inválido: {intervalo}")

    semitons = INTERVALOS_NORMALIZADOS[intervalo_normalizado]
    return transpor_nota(nota_inicial,semitons)

