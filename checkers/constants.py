import pygame

#Width => Largura, Width => Altura
WIDTH, HEIGHT = 450, 450
#Rows => Linhas, Cols => Colunas
ROWS, COLS = 8, 8
#SQUARE_SIZE => É o resto divisão de largura por Colunas
SQUARE_SIZE = WIDTH//COLS

#COLOR for the game
GREY = (186, 186, 186)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (217, 97, 11)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (34, 25))