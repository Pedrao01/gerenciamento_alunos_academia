from gerar_arquivo import manipular_arquivo


def pagamento_aluno(arquivo, aluno):
    with open(arquivo, 'r') as a:
        alunos = []
        for linha in a.readlines():
            li = linha.split(';')
            if aluno != li[0]:
                alunos.append(linha)
                print('não pagou')
            else:
                #atualizar a data de pagamento
        remover(arquivo, alunos)


def remover(arquivo_novo, alunos):
    with open(arquivo_novo, 'w') as file:
        print(alunos)
        cont = 0
        for p in alunos:
            cont += 1
            file.write(p)
            # if cont != len(alunos):
            #     file.write('\n')


# pagamento_aluno('alunos_com_pagamento_atrasado', ['andrey','20.10.2024','50','pedro','\n'])