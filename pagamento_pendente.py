from datetime import datetime, timedelta
from gerar_arquivo import devedores


def tratar(file_name):
    with open(file_name, 'r') as file:
        cont = 0
        for num_linha, line in enumerate(file.readlines(), start=1):
            lv = line.split(';')
            lv.pop()
            cont += 1
            pendentes(lv, cont)


def pendentes(lista, numero_linhas):
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
        devedores('alunos_com_pagamento_atrasado', lista, numero_linhas)
    # if :
    #     # print('atrasou pagamento')
    #     devedores('alunos_com_pagamento_atrasado', lista, numero_linhas)


tratar('alunos_academia')