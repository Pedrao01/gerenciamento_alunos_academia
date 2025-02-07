from interface import interface, perguntas, titulo, mostrar
from aluno import Aluno
from pagamento import pagamento_aluno
from pagamento_pendente import tratar

while True:
    tratar('alunos_academia')
    titulo('gym app', caractere='=')
    escolha = interface()

    if escolha == 1:
        titulo('add new studant', caractere='-')
        informações_aluno = perguntas()
        aluno = Aluno(informações_aluno)
        aluno.adicionar_novo_aluno()
    elif escolha == 2:
        print('pagou')
        nome_aluno = str(input('Nome do aluno: '))
        pagamento_aluno('alunos_com_pagamento_atrasado','alunos_academia', nome_aluno)
    elif escolha == 3:
        print('ver alunos pendentes')
        mostrar('alunos_com_pagamento_atrasado')
    else:
        print('sair')
        break