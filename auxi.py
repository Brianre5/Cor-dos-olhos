from classes import pessoa, geracao
import numpy as np


def passar_geracao(geracao_atual):
    NUMERO_DE_PESSOAS = geracao_atual.n
    nova_geracao = geracao(NUMERO_DE_PESSOAS, geracao_atual.idade + 1)
    i = 0
    while i < NUMERO_DE_PESSOAS / 2:
        aleatorio = np.random.randint(0, NUMERO_DE_PESSOAS)
        indice = i
        while geracao_atual.comunidade[indice].teve_filho:
            indice = (indice + 1) % NUMERO_DE_PESSOAS
        while geracao_atual.comunidade[aleatorio].teve_filho:
            aleatorio = (aleatorio + 1) % NUMERO_DE_PESSOAS
        geracao_atual.comunidade[indice].definir_parceiro(
            geracao_atual.comunidade[aleatorio]
        )
        pessoa_nova = geracao_atual.comunidade[indice].fazer_filho()
        nova_geracao.comunidade[i] = pessoa_nova
        i += 1
    for j in range(NUMERO_DE_PESSOAS):
        geracao_atual.comunidade[j].teve_filho = False

    while i < NUMERO_DE_PESSOAS:
        aleatorio = np.random.randint(0, NUMERO_DE_PESSOAS)
        indice = i
        while geracao_atual.comunidade[indice].teve_filho:
            indice = (indice + 1) % NUMERO_DE_PESSOAS
        while geracao_atual.comunidade[aleatorio].teve_filho:
            aleatorio = (aleatorio + 1) % NUMERO_DE_PESSOAS
        geracao_atual.comunidade[indice].definir_parceiro(
            geracao_atual.comunidade[aleatorio]
        )
        pessoa_nova = geracao_atual.comunidade[indice].fazer_filho()
        nova_geracao.comunidade[i] = pessoa_nova
        i += 1
    nova_geracao.calcular_pct()
    return nova_geracao
