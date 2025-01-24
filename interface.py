def interface():
    print("""1. adicionar novo aluno
2. ver alunos pendentes
3. sair do programa
""")
    escolha = int(input('qual deseja: '))
    return escolha


def perguntas():
    while True:
        nome = str(input('nome do aluno: ')).strip()
        data = str(input('data que entrou[separe por um "."]: ')).strip()
        valor = str(input('valor pago: ')).strip()
        treinador = str(input('treinador: ')).strip()
        aluno = [nome, data, valor, treinador]
        if '' not in aluno:
            return aluno
        else:
            mensagens('não pode haver valo nulo ou em branco')


def titulo(msg):
    print('===='*len(msg))
    print(msg.center(len(msg)*4))
    print('===='*len(msg))


def subtitulo(msg):
    print('--' * len(msg))
    print(msg.center(len(msg)*2))
    print('--' * len(msg))


def mensagens(msg):
    print('*' * (len(msg) + 4))
    print('*', msg.center(len(msg)), '*')
    print('*' * (len(msg) + 4))
