def manipular_arquivo(nome_arquivo, informacoes_aluno):

    try:
        with open(nome_arquivo, 'a+') as arquivo:
            for c in informacoes_aluno:
                arquivo.write(c)
                arquivo.write(';')
            arquivo.write('\n')
    except FileNotFoundError:
        with open(nome_arquivo, 'w') as arquivo:
            for c in informacoes_aluno:
                arquivo.write(c)
                arquivo.write(';')
            arquivo.write('\n')
