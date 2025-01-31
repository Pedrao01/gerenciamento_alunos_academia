from interface import interface, perguntas, titulo, subtitulo, mensagens
from aluno import Aluno
from pagamento import pagamento_aluno
from pagamento_pendente import tratar
# from gerar_arquivo import manipular_arquivo

while True:
    tratar('alunos_academia')
    titulo('gym app')
    escolha = interface()

    if escolha == 1:
        subtitulo('add new studant')
        informações_aluno = perguntas()
        aluno = Aluno(informações_aluno)
        aluno.adicionar_novo_aluno()
    elif escolha == 2:
        print('pagou')
        nome_aluno = str(input('Nome do aluno: '))
        pagamento_aluno('alunos_com_pagamento_atrasado', nome_aluno)
    elif escolha == 3:
        print('ver alunos pendentes')
    else:
        print('sair')
        break