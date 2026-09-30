from models.maestro import SolicitacaoAula
from services.maestro import gerar_aula
# from tools.musica import transpor_nota


solicitacao = SolicitacaoAula(
    pergunta="O que é uma Função dominante secundaria e como ela se relaciona com a progressão harmônica em uma música?",
    nivel_aluno="avancado",
    instrumento_escolhido="violao",
)

print(gerar_aula(solicitacao))