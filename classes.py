import numpy as np


class pessoa:
    def __init__(self, pai, mae, cor):
        self.pai = [pai, mae]
        self.cor = cor
        self.parceiro = None
        self.teve_filho = False

    def definir_parceiro(self, pessoa):
        self.parceiro = pessoa
        pessoa.parceiro = self

    def fazer_filho(self):
        epsilon = np.random.uniform(0, 1)
        cor_do_filho = 3
        if self.parceiro == None:
            print("Erro, sem parceiro!")

        cores = {self.cor, self.parceiro.cor}
        # MARROM == 0
        # VERDE == 1
        # AZUL == 2
        # Marrom - Marrom
        if cores == {0}:
            if epsilon < 0.0625:
                cor_do_filho = 2
            elif epsilon < 0.25:
                cor_do_filho = 1
            else:
                cor_do_filho = 0
        # Verde - Verde
        if cores == {1}:
            if epsilon < 0.25:
                cor_do_filho = 2
            elif epsilon < 0.995:
                cor_do_filho = 1
            else:
                cor_do_filho = 0
        # Azul - Azul
        if cores == {2}:
            if epsilon < 0.99:
                cor_do_filho = 2
            else:
                cor_do_filho = 1
        # Marrom - Azul
        if cores == {0, 2}:
            if epsilon < 0.5:
                cor_do_filho = 0
            else:
                cor_do_filho = 2
        # Marrom - Verde
        if cores == {0, 1}:
            if epsilon < 0.375:
                cor_do_filho = 1
            elif epsilon < 0.5:
                cor_do_filho = 2
            else:
                cor_do_filho = 0
        # Azul - Verde
        if cores == {1, 2}:
            if epsilon < 0.5:
                cor_do_filho = 1
            else:
                cor_do_filho = 2

        filho = pessoa(self, self.parceiro, cor_do_filho)
        self.teve_filho = True
        self.parceiro.teve_filho = True
        return filho


class geracao:
    def __init__(self, n_pessoas, idade):
        self.idade = idade
        self.n = n_pessoas
        self.comunidade = [None] * n_pessoas
        self.pct_azul = 0
        self.pct_verde = 0
        self.pct_marrom = 0

    def popular_geracao(self, pct_marrom, pct_verde, pct_azul):
        self.pct_azul = pct_azul
        self.pct_verde = pct_verde
        self.pct_marrom = pct_marrom
        for i in range(self.n):
            if i <= pct_marrom * self.n / 100:
                self.comunidade[i] = pessoa(None, None, 0)
            elif i <= (pct_marrom + pct_verde) * self.n / 100:
                self.comunidade[i] = pessoa(None, None, 1)
            elif i <= (pct_marrom + pct_verde + pct_azul) * self.n / 100:
                self.comunidade[i] = pessoa(None, None, 2)

    def calcular_pct(self):
        azul = 0
        verde = 0
        marrom = 0
        for i in range(self.n):
            if self.comunidade[i].cor == 0:
                marrom += 1
            if self.comunidade[i].cor == 1:
                verde += 1
            if self.comunidade[i].cor == 2:
                azul += 1
        self.pct_azul = int(azul / self.n * 100)
        self.pct_marrom = int(marrom / self.n * 100)
        self.pct_verde = int(verde / self.n * 100)
