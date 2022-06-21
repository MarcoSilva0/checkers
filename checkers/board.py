#Class reposability for create the board of game
import pygame
from .constants import BLACK, ROWS, GREY, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        #Qtd of parts of player and IA exists
        self.grey_left = self.white_left = 12
        #Qtd of Queens of player and IA exists
        self.grey_queens = self.white_queens = 0

    #Draw de houses of parts
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    #Draw full bord with pieces 