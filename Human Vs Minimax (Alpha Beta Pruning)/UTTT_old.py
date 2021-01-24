import pygame
import os
import sys
import random
from math import inf as infinity

from Board import new_Board

from Frontend import fill
from Frontend import Draw_pieces
from Frontend import draw_board
from Frontend import draw_big_pieces

from Check_game import Check_Big_Board, empty_cells_big_board, Check_empty_cells, check_game, empty_cells_small_boards
from Check_game import check_game
from Check_game import set_locations
from Check_game import get_possible_moves, Validate_box
from minimax import Minimax

from inspect import signature

sign = signature(set_locations)
params = sign.parameters
print(params)
print(len(params))



pygame.font.init()
Width, Height = 792,792
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

def ai_turn(small_boards, main_board, turn, box):
    if small_boards[4][4] == 0 and turn == 1 and [4,4] in box:
        new_board = copy.deepcopy(small_boards)
        new_board[4][4] = 1
        return new_board
    else:
        alpha, beta = -infinity, +infinity
        depth = 2
        value, new_board = Minimax(small_boards, main_board, depth, 1, alpha, beta, box, True)
        print("new b : ", new_board)
        print("final score : ", value)
        return new_board


def update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Small_Cross, Small_Circle, Cross, Circle,board,big_board, player):
    Win.fill(Bg)
    Draw_pieces(Win,Small_Cross, Small_Circle,Cross, Circle, Small_Square, Square, board)
    draw_board(Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin)
    draw_big_pieces(Win, big_board, Square, Circle, Cross)
    pygame.display.update()



main_board = Game_Board.create_board()
small_boards = Game_Board.every_small_boards()

def main(small_boards, main_board):
    print("Welcome ! ")
    run = True
    #turn = random.choice([-1,1])
    AI = 1
    HUMAN = -1
    turn = HUMAN
    FPS = 120
    green = (0,178,0,0)
    game_over = False
    good = False

    box = None

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
                        x = pos[0]//(Small_Square)
                        y = pos[1]//(Small_Square)

                        if set_locations(small_boards, main_board, x, y, turn):
                            check_game(small_boards, main_board,turn)

                            new_box = get_possible_moves(small_boards,pos[0]//(Small_Square), pos[1]//(Small_Square))
                            #print("box after get_possible_moves", new_box)
                            box = Validate_box(small_boards, main_board, new_box,pos[0]//(Small_Square), pos[1]//(Small_Square))
                            #print("Box validated", box)
                            turn = -1

                        if Check_Big_Board(main_board, HUMAN):
                            game_over = True


                    #update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Cross_small, Circle_small, Cross, Circle, small_boards, main_board, turn)

        if turn == AI and not game_over:

            new_board = ai_turn(small_boards, main_board, turn, box)
            small_boards = new_board
            check_game(small_boards,main_board, turn)

            print("small_boards : ", small_boards)
            if Check_Big_Board(main_board, turn):
                game_over = True

            turn = HUMAN

        update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Cross_small, Circle_small, Cross, Circle, small_boards, main_board, turn)


main(small_boards, main_board)