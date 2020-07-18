import pygame
import os
import sys
import random
from Board import new_Board

pygame.font.init()
Width, Height = 770,770
Square = Width//3
Small_Square = Square//3
margin = Width//20

Win = pygame.display.set_mode((Width, Height))

Cross_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Small_Square, Small_Square))
Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Square, Square))

Circle_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Small_Square, Small_Square))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Square, Square))


Bg = (255,255,255)
Lines_color = (211,211,211)
Lines_color_2 = (250, 0, 0)


AI = 1
HUMAN = -1

Game_Board = new_Board()


def update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin):
    Win.fill(Bg)
    Game_Board.draw_board(Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin)
    pygame.display.update()

main_board = Game_Board.create_board()
small_boards = Game_Board.every_small_boards()

print(main_board)
print(small_boards)

def main():
    run = True
    Game_Board.test()
    while run:
        update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

main()
