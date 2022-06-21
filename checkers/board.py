#Class reposability for create the board of game
from cmath import pi
import pygame

from checkers.piece import Piece
from .constants import GREY, WHITE, ROWS, BLACK, SQUARE_SIZE, COLS, ORANGE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        #Qtd of parts of player and IA exists
        self.grey_left = self.white_left = 12
        #Qtd of Queens of player and IA exists
        self.black_queens = self.white_queens = 0
        #I call the board creator when starting
        self.create_board()

    #Draw de houses of parts
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS or row == 0:
            piece.make_queen()
            if piece.color == WHITE:
                self.white_queens += 1
            else:
                self.black_queens += 1
            
    def get_piece(self, row, col):
        return self.board[row][col]
        

    #Draw full bord with pieces 
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    #I only draw on lines 3 or less and 6 or greater
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, ORANGE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)