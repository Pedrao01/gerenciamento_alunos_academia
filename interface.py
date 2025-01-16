def interface():
    print("""1. adicionar novo aluno
2. ver alunos pendentes
3. sair do programa
""")
    escolha = int(input('qual deseja: '))
    return escolha


def perguntas():
    nome = str(input('nome do aluno: '))
    data = str(input('data que entrou[dia/mês/ano]: '))
    valor = str(input('valor pago: '))
    treinador = str(input('treinador: '))
    aluno = [nome, data, valor, treinador]
    return aluno