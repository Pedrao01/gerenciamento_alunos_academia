def pagamento_aluno(arquivo_atrasado, arquivo_alunos, nome_aluno):
    with open(arquivo_atrasado, 'r') as a:
        alunos = []
        for linha in a.readlines():
            li = linha.split(';')
            if nome_aluno != li[0]:
                alunos.append(linha)
                # print('não pagou')
            else:
                pagamento(arquivo_alunos, nome_aluno)

        reescrever(arquivo_atrasado, alunos)


def reescrever(arquivo_novo, alunos):
    with open(arquivo_novo, 'w') as file:
        for p in alunos:
            file.write(p)


def pagamento(arquivo_alunos, nome_aluno):
    from datetime import datetime
    with open(arquivo_alunos, 'r') as arq:
        alunos = []
        for linha in arq.readlines():
            li = linha.split(';')
            if nome_aluno != li[0]:
                alunos.append(linha)
            else:
                today = str(datetime.now().date()).split('-')

                today.reverse()

                today_str = lista_para_str(today, '.')
                li[1] = today_str

                n = lista_para_str(li, ';')
                alunos.append(n)
        reescrever(arquivo_alunos, alunos)


def lista_para_str(lista, caracter):
    nova_str = ''
    for i in lista:
        nova_str += i
        nova_str += caracter
    n = nova_str[:-1]
    return n
