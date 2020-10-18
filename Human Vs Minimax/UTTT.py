import pygame
import os
import sys
import random
from math import inf as infinity

from Board import new_Board, set_locations, valid_locations

from Frontend import fill
from Frontend import Draw_pieces
from Frontend import draw_board
from Frontend import draw_big_pieces

from Check_game import Check_horizontally, Check_vertically, Check_diagonals, Check_Big_Board, empty_cells_big_board, Check_empty_cells, check_game

from minimax import random_piece, minimax_algo

import copy

pygame.font.init()
Width, Height = 810,810
Square = Width//3
Small_Square = Square//3
margin = Width//30

Win = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()

Cross_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Small_Square, Small_Square))
Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cross.png")), (Square, Square))

Circle_small = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Small_Square, Small_Square))
Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "circle.png")), (Square, Square))

Bg = (0,0,0)
Lines_color = (211,211,211)
Lines_color_2 = (250, 0, 0)

Game_Board = new_Board()



def update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Small_Cross, Small_Circle, Cross, Circle,board,big_board, player):
    Win.fill(Bg)
    Draw_pieces(Win,Small_Cross, Small_Circle,Cross, Circle, Small_Square, Square, board)
    draw_board(Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin)
    draw_big_pieces(Win, big_board, Square, Circle, Cross)
    pygame.display.update()

def ai_turn(board, small_boards, turn):
    small_boards = board
    turn = -1

main_board = Game_Board.create_board()
small_boards = Game_Board.every_small_boards()

def main(small_boards, main_board):
    run = True
    turn = random.choice([-1,1])
    AI = 1
    HUMAN = -1

    FPS = 120
    green = (0,178,0,0)
    game_over = False
    good = False

    while run:
        clock.tick(FPS)
        fill(Circle_small,green)
        fill(Circle, green)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    Game_Board.reset(small_boards, main_board, game_over)
                    game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN and turn == HUMAN and not game_over:
                if pygame.mouse.get_pressed()[0] and turn == HUMAN and not game_over:
                    pos = pygame.mouse.get_pos()
                    if turn == HUMAN and not game_over:
                        set_locations(small_boards, main_board, pos[0]//(Small_Square), pos[1]//(Small_Square), turn)
                        check_game(small_boards, main_board,turn)

                        if Check_Big_Board(main_board, turn):
                            game_over = True

                        turn = AI

        if turn == AI and not game_over:
            depth = 1
            alpha, beta = -infinity, +infinity
            value, x,y = minimax_algo(small_boards, main_board, 2, turn,True)
            print("x,y", x,y)
            #board = random_piece(small_boards, main_board, turn)
            set_locations(small_boards, main_board, x,y, turn)
            check_game(small_boards,main_board, turn)
            if Check_Big_Board(main_board, turn):
                game_over = True

            turn = HUMAN

        update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Cross_small, Circle_small, Cross, Circle, small_boards, main_board, turn)


main(small_boards, main_board)
