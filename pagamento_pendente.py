from datetime import datetime


def tratar(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            print(line)
            lv = line.split(';')
            lv.pop()
            pendentes(lv)


def pendentes(lista):
    date_start = lista[1].split('.')
    date_start.reverse()

    today = str(datetime.now().date()).split('-')

    for c in range(0, 3):
        date_start[c] = int(date_start[c])
        today[c] = int(today[c])
    print(date_start, today)


tratar('alunos_academia')