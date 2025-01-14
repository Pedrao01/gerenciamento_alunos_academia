from interface import interface
# from aluno import Aluno
# from gerar_arquivo import manipular_arquivo
while True:
    escolha = interface()
    if escolha == 1:
        print('adicionar novo aluno')
    elif escolha == 2:
        print('ver alunos pendentes')
    else:
        print('sair')
        break