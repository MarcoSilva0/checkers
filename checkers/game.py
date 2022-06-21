import pygame
from checkers.board import Board
from checkers.piece import Piece
from .constants import SQUARE_SIZE, WHITE, ORANGE, GREEN

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = ORANGE
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.select = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
        #I would cant use skipped but this is most confused
        else:
            return False
        
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, GREEN, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        if self.turn == ORANGE:
            self.turn = WHITE
        else:
            self.turn = ORANGE