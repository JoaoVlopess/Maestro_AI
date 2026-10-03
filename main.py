from models.maestro import SolicitacaoAula
from services.maestro import gerar_aula
# from tools.musica import transpor_nota


solicitacao = SolicitacaoAula(
    pergunta="O que é cifra? Para que ela serve e quais as principais modificações que podem ser feitas em um acorde na cifra?",
    nivel_aluno="intermediario",
    instrumento_escolhido="violao",
)

print(gerar_aula(solicitacao))