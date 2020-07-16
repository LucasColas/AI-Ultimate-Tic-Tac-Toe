import pygame
import os
import sys
import random
import Board

pygame.font.init()
Width, Height = 770,770
Square = Width//3
Small_Square = Square//3

Win = pygame.display.set_mode((Width, Height))

Cross_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Small_Square, Small_Square))
Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Square, Square))

Circle_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Small_Square, Small_Square))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Square, Square))



Bg = (255,255,255)
Lines_color = (211,211,211)


AI = 1
HUMAN = -1

Game_Board = new_Board()


def update_window(Win, Lines_color, Width):
    Win.fill(Bg)
    Game_Board.draw_board(Win, Lines_color, Width)
    pygame.display.update()

def main():
    run = True
    Game_Board.test()
    while run:
        update_window(Win, Lines_color, Width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

main()
