from gerar_arquivo import abrir_arquivo


class Aluno:
    def __init__(self, nome, data, valor):
        self.nome = nome
        self.data = data
        self.valor = valor

    def adicionar_novo_aluno(self):
        abrir_arquivo('alunos_academia',self.nome, self.data, self.valor)


pedro = Aluno('pedro duarte', '12/01/2025', 40)
pedro.adicionar_novo_aluno()