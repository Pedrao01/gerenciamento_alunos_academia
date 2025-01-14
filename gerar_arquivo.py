
def manipular_arquivo(nome_arquivo, nome_aluno, data, valor):
    lista = [nome_aluno, data, str(valor)]
    try:
        with open(nome_arquivo, 'a+') as arquivo:
            for c in lista:
                arquivo.write(c)
                arquivo.write(';')
            arquivo.write('\n')
    except FileNotFoundError:
        with open(nome_arquivo, 'w') as arquivo:
            for c in lista:
                arquivo.write(c)
                arquivo.write(';')
            arquivo.write('\n')
