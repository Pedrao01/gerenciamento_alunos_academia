import datetime


def tratar(file_name):
    with open(file_name, 'r') as file:
        for line in file.readlines():
            print(line)
            lv = line.split(';')
            lv.pop()
            pendentes(lv)


def pendentes(lista):
    print(lista[1])


tratar('alunos_academia')