import pygame
import os
import sys
import random

from Board import new_Board

from Frontend import fill
from Frontend import Draw_pieces
from Frontend import draw_board

print("test")

pygame.font.init()
Width, Height = 800,800
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

def check_game(board,main_board, good, player):

    #Check horizontally
    for i in range(0,7,3):
        for indx, row in enumerate(board):
            if row[0+i] == row[1+i] == row[2+i] == player:
                print(player, "horizontal")
                good = True
                print(good)
                return [i,indx, good]

    #Check vertically
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
            if len(check) == 3:
                if check.count(player) == len(check) and check[0] != 0:
                    print(player, "succeeds")

                else:
                    check.clear()

def place_big_board(board, main_board, player):

    i, indx,good = check_game(board, main_board, player)
    main_board[indx//3][i] = player

def reset(board, main_board, game_over):
    if game_over:
        for x,row in enumerate(board):
            for y in range(len(row)):
                board[y][x] = 0

def update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Small_Cross, Small_Circle, Cross, Circle,board,big_board, player):
    Win.fill(Bg)
    draw_board(Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin)
    Draw_pieces(Win,Small_Cross, Small_Circle,Cross, Circle, Small_Square, Square, board, big_board, player)
    pygame.display.update()


def main():
    run = True
    turn = -1
    AI = 1
    HUMAN = -1
    Game_Board.test()

    green = (0,178,0,0)

    game_over = False
    good = False

    main_board = Game_Board.create_board()
    small_boards = Game_Board.every_small_boards()

    print(main_board)
    print(small_boards)
    while run:
        fill(Circle_small,green)
        fill(Circle, green)
        update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Cross_small, Circle_small, Cross, Circle, small_boards, main_board, turn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN and game_over:
                reset(small_boards, main_board, game_over)
                game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN and turn == HUMAN and not game_over:
                if pygame.mouse.get_pressed()[0] and turn == HUMAN and not game_over:
                    pos = pygame.mouse.get_pos()
                    if turn == HUMAN and not game_over:
                        print("Yes", pos[0]//(Small_Square), pos[1]//(Small_Square))
                        set_locations(small_boards, pos[0]//(Small_Square), pos[1]//(Small_Square), turn)
                        check_game(small_boards, main_board,good,turn)
                        print(good)
                        if good:
                            place_big_board(small_boards, main_board, good, turn)
                            good = False

                        print(small_boards)
                        print(main_board)


main()
