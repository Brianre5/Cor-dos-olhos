import pygame
import numpy as np
import math
from classes import pessoa, geracao
from auxi import passar_geracao

# CONSTANTS
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
NUMERO_DE_PESSOAS = 64 * 64
PORCENTAGEM_MARROM = 83  # 70 - 80
PORCENTAGEM_VERDE = 14  # 5 - 12
PORCENTAGEM_AZUL = 3  # 8 - 10
TABELA = [(139, 69, 19), (0, 255, 0), (0, 0, 255)]

# INITIALIZE THE GENERATION 0
geracao_atual = geracao(NUMERO_DE_PESSOAS, 0)
geracao_atual.popular_geracao(PORCENTAGEM_MARROM, PORCENTAGEM_VERDE, PORCENTAGEM_AZUL)


# Initialize the pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simulação da cor dos olhos")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font("freesansbold.ttf", 32)

# Pygame Loop
running = True
previous_keys = pygame.key.get_pressed()


def process_inputs(keys, previous_keys):
    global geracao_atual
    if keys[pygame.K_SPACE] and not previous_keys[pygame.K_SPACE]:
        geracao_atual = passar_geracao(geracao_atual)


def mostrar_pessoas():
    RAIZ = int(math.sqrt(NUMERO_DE_PESSOAS))
    LARGURA = (SCREEN_WIDTH - 10) / RAIZ
    ALTURA = (SCREEN_HEIGHT - 200 - 10) / RAIZ
    for i in range(NUMERO_DE_PESSOAS):
        humano = geracao_atual.comunidade[i]
        color = TABELA[humano.cor]
        x = 5 + LARGURA * (i % RAIZ)
        y = 5 + ALTURA * int(i / RAIZ)
        pygame.draw.rect(screen, color, (x, y, LARGURA, ALTURA))


def escrever_na_tela():
    pygame.draw.line(
        screen,
        (0, 0, 0),
        (0, SCREEN_HEIGHT - 205),
        (SCREEN_WIDTH, SCREEN_HEIGHT - 205),
        2,
    )
    gen_text = font.render("GERAÇÃO: " + str(geracao_atual.idade), True, (0, 0, 0))
    screen.blit(gen_text, (5, SCREEN_HEIGHT - 200))
    marrom_text = font.render(
        "MARROM: " + str(geracao_atual.pct_marrom), True, (0, 0, 0)
    )
    screen.blit(marrom_text, (300, SCREEN_HEIGHT - 200))
    verde_text = font.render("VERDE: " + str(geracao_atual.pct_verde), True, (0, 0, 0))
    screen.blit(verde_text, (5, SCREEN_HEIGHT - 100))
    azul_text = font.render("AZUL: " + str(geracao_atual.pct_azul), True, (0, 0, 0))
    screen.blit(azul_text, (300, SCREEN_HEIGHT - 100))


while running:
    clock.tick(30)
    keys = pygame.key.get_pressed()
    screen.fill((255, 255, 255))
    process_inputs(keys, previous_keys)
    mostrar_pessoas()
    escrever_na_tela()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    previous_keys = keys
    pygame.display.update()
