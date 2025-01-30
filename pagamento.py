def pagamento_aluno(arquivo, aluno):
    with open(arquivo, 'r') as a:
        alunos = []
        for linha in a.readlines():
            linha = linha.replace('\n', '')
            if aluno != linha:
                alunos.append(linha)
                print(linha)
                print('não pagou')
        remover(arquivo, alunos)


def remover(arquivo_novo, alunos):
    with open(arquivo_novo, 'w') as file:
        for p in alunos:
            file.write(p)
            file.write('\n')


pagamento_aluno('alunos_com_pagamento_atrasado', 'manel;28.01.2025;40;pedro;')