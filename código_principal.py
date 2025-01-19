from interface import interface
from interface import perguntas
from interface import titulo
from interface import mensagens
from aluno import Aluno
# from gerar_arquivo import manipular_arquivo
while True:
    titulo('App da academia')
    escolha = interface()
    if escolha == 1:
        mensagens('adicionar novo aluno')
        informações_aluno = perguntas()
        aluno = Aluno(informações_aluno)
        aluno.adicionar_novo_aluno()
    elif escolha == 2:
        print('ver alunos pendentes')
    else:
        print('sair')
        break