def interface():
    print("""1. adicionar novo aluno
2. ver alunos pendentes
3. sair do programa
""")
    escolha = int(input('qual deseja: '))
    return escolha


def perguntas():
    nome = str(input('nome do aluno: ')).strip()
    data = str(input('data que entrou[dia/mês/ano]: ')).strip()
    valor = str(input('valor pago: ')).strip()
    treinador = str(input('treinador: ')).strip()
    aluno = [nome, data, valor, treinador]
    return aluno


def titulo(msg):
    print('='*30)
    print(msg.center(30))
    print('='*30)


def mensagens(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)