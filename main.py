import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
#Here I drawn basic forms geme
#The FPS const not included in constants because this info is important for me(user) no important for the game
FPS = 60

#Draw primary window, the vars width and height I get from checkers/constants.py
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

#
def main():
    run = True
    #The clock is for define the game FPS for equalize the for all user PC
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            #Look evets, this event look if user want exit the game
            if event.type == pygame.QUIT:
                run = False
            
            #Look the event click of the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()