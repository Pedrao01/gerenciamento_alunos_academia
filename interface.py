def interface():
    while True:
        print("""
    1. adicionar novo aluno
    2. pagamento
    3. ver alunos pendentes
    0. sair do programa
    """)
        escolha = input('qual deseja: ')
        if escolha.isdigit():
            if 0 <= int(escolha) <= 3:
                return int(escolha)
            else:
                print('escolha a opção de 0 até 3')
        else:
            print('digite apenas números')


def perguntas():
    while True:
        nome = str(input('nome do aluno: ')).strip()
        data = str(input('data que entrou ou entrou[separe por um "."]: ')).strip()
        valor = str(input('valor pago: ')).strip()
        treinador = str(input('treinador: ')).strip()
        aluno = [nome, data, valor, treinador]
        if '' not in aluno:
            return aluno
        else:
            mensagens('não pode haver valo nulo ou em branco')


def titulo(msg, caractere, num=69):
    print(caractere*num)
    print(msg.center(num))
    print(caractere*num)


def mensagens(msg):
    print('*' * (len(msg) + 4))
    print('*', msg.center(len(msg)), '*')
    print('*' * (len(msg) + 4))


def mostrar(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        informacoes = ['nome', 'data', 'valor', 'treinador']
        print('-' * 69)
        for i in informacoes:
            print(i.ljust(20), end='')
        print()
        print('-' * 69)
        lista_valores = arquivo.readlines()
        for v in lista_valores:
            linha = v[:-2]
            linha = linha.split(';')
            for msg in linha:
                print(msg.ljust(20), end='')
            print()
        print()
