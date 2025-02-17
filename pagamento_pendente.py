from datetime import datetime, timedelta
from gerar_arquivo import devedores
from pathlib import Path


def tratar(file_name):
    arquivo = Path('alunos_com_pagamento_atrasado.txt')
    if not arquivo.exists():
        print('arquivo criado')
        with open('alunos_com_pagamento_atrasado.txt', 'w') as a:
            print()

    with open(file_name, 'r') as file:
        cont = 0
        for num_linha, line in enumerate(file.readlines(), start=1):
            lv = line.split(';')
            lv.pop()
            cont += 1
            pendentes(lv, cont)


def pendentes(lista, numero_linhas):
    aluno_na_lista = True
    if numero_linhas != 1:
        aluno_na_lista = verificar_aluno('alunos_com_pagamento_atrasado.txt', lista)
    if aluno_na_lista:
        date_start = lista[1].split('.')
        date_start.reverse()

        today = str(datetime.now().date()).split('-')

        for c in range(0, 3):
            date_start[c] = int(date_start[c])
            today[c] = int(today[c])

        instant1 = datetime(*date_start)
        instant2 = datetime(*today)
        diferenca = instant2 - instant1

        if diferenca == timedelta(days=31) or diferenca > timedelta(days=31):
            # print('dia do pagamento')
            devedores('alunos_com_pagamento_atrasado.txt', lista, numero_linhas)


def verificar_aluno(nome_arquivo, nome_aluno):
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo.readlines():
            linha = linha.split(';')
            print(linha[0], nome_aluno[0])
            if linha[0] == nome_aluno[0]:
                return False
        else:
            return True
