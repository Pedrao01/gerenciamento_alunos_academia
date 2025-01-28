from datetime import datetime, timedelta
from gerar_arquivo import devedores


def tratar(file_name):
    with open(file_name, 'r') as file:
        cont = 0
        for num_linha, line in enumerate(file.readlines(), start=1):
            print(line)
            lv = line.split(';')
            lv.pop()
            cont += 1
            print(cont)
            pendentes(lv, cont)


def pendentes(lista, numero_linhas):
    date_start = lista[1].split('.')
    date_start.reverse()

    today = str(datetime.now().date()).split('-')

    for c in range(0, 3):
        date_start[c] = int(date_start[c])
        today[c] = int(today[c])
    print(date_start, today)

    instant1 = datetime(*date_start)
    instant2 = datetime(*today)
    diferenca = instant2 - instant1
    print(type(diferenca))
    if diferenca == timedelta(days=31):
        print('dia do pagamento')

    if diferenca > timedelta(days=31):
        print('atrasou pagamento')
        print(numero_linhas)
        devedores('alunos_com_pagamento_atrasado', lista, numero_linhas)
    print(diferenca)


tratar('alunos_academia')