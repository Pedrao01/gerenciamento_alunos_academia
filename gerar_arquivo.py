def abrir_arquivo(nome_arquivo, nome_aluno, data, valor):
    lista = [nome_aluno, data, str(valor)]
    with open(nome_arquivo, 'w') as arquivo:
        for c in lista:
            arquivo.write(c)
            arquivo.write(';')
        arquivo.write('\n')
