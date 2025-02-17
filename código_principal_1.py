from interface import interface, perguntas, titulo, mostrar, mensagens
from aluno import Aluno
from pagamento import pagamento_aluno
from pagamento_pendente import tratar
from pathlib import Path

while True:
    titulo('gym app', caractere='=')
    arquivo = Path('alunos_academia')
    escolha = interface()
    if escolha == 1:
        titulo('add new studant', caractere='-')
        informações_aluno = perguntas()
        aluno = Aluno(informações_aluno)
        aluno.adicionar_novo_aluno()
    if arquivo.exists():
        if escolha == 2:
            print('pagou')
            nome_aluno = str(input('Nome do aluno: '))
            pagamento_aluno('alunos_com_pagamento_atrasado.txt', 'alunos_academia', nome_aluno)
        elif escolha == 3:
            print('ver alunos pendentes')
            tratar('alunos_academia')
            mostrar('alunos_com_pagamento_atrasado.txt')
        elif escolha == 0:
            print('sair')
            break
    else:
        mensagens('Não há alunos salvos. Escolha a opção 1, para começar.')
