import pygame
import os
import sys
import random
from Board import new_Board

pygame.font.init()
Width, Height = 770,770
Square = Width//3
Small_Square = Square//3
margin = Width//30

Win = pygame.display.set_mode((Width, Height))

Cross_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Small_Square, Small_Square))
Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Square, Square))

Circle_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Small_Square, Small_Square))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Square, Square))


Bg = (255,255,255)
Lines_color = (211,211,211)
Lines_color_2 = (250, 0, 0)


Game_Board = new_Board()

def valid_locations(board,x,y):
    for row in board:
        for col in row:
            if board[y][x] == 0:
                print("Valid")
                return True

def set_locations(board,x,y, player):
    if valid_locations(board,x,y):
        board[y][x] = player
        return True
    else:
        return False

def check_game(board,main_board, player):
    for i in range(0,7,3):
        for row in board:
            if row[0+i] == row[1+i] == row[2+i] == player:
                print(player, "wins")


def update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin):
    Win.fill(Bg)
    Game_Board.draw_board(Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin)
    pygame.display.update()


def main():
    run = True
    turn = -1
    AI = 1
    HUMAN = -1
    Game_Board.test()

    game_over = False
    main_board = Game_Board.create_board()
    small_boards = Game_Board.every_small_boards()

    print(main_board)
    print(small_boards)
    while run:
        update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN and turn == HUMAN and not game_over:
                if pygame.mouse.get_pressed()[0] and turn == HUMAN and not game_over:
                    pos = pygame.mouse.get_pos()
                    if turn == HUMAN and not game_over:
                        print("Yes", pos[0]//(Small_Square), pos[1]//(Small_Square))
                        set_locations(small_boards, pos[0]//(Small_Square), pos[1]//(Small_Square), turn)
                        check_game(small_boards, main_board,turn)
                        print(small_boards)


main()
