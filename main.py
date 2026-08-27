from models.maestro import SolicitacaoAula
from services.maestro import gerar_aula
# from tools.musica import transpor_nota


solicitacao = SolicitacaoAula(
    pergunta="O que é um intervalo musical? Me de um exemplo de diversos intervalos diferentes partindo de A#.",
    nivel_aluno="avancado",
    instrumento_escolhido="guitarra",
)

print(gerar_aula(solicitacao))