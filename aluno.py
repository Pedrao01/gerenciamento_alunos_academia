from gerar_arquivo import manipular_arquivo


class Aluno:
    def __init__(self, informacoes_aluno):
        self.informacoes_aluno = informacoes_aluno
        # self.nome = nome
        # self.data = data
        # self.valor = valor
        # self.treinador = treinador

    def adicionar_novo_aluno(self):
        manipular_arquivo('alunos_academia', self.informacoes_aluno)


# pedro = Aluno('pedro duarte', '13/09/2023', 50)
# pedro.adicionar_novo_aluno()