import pygame
import os
import sys
import random

from Board import new_Board

from Frontend import fill
from Frontend import Draw_pieces
from Frontend import draw_board
from Frontend import draw_big_pieces

from Check_game import Check_horizontally, Check_vertically, Check_diagonals, Check_Big_Board, empty_cells_big_board, Check_empty_cells
from Check_game import get_possible_moves
from Check_game import Validate_box
from Check_game import valid_locations, set_locations
from Check_game import check_game

from minimax import Minimax



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


def main():
    run = True
    turn = random.choice([-1,1])
    AI = 1
    Human = -1
    #Game_Board.test()

    FPS = 120
    green = (0,178,0,0)
    game_over = False
    good = False


    box = None

    main_board = Game_Board.create_board()
    small_boards = Game_Board.every_small_boards()

    while run:

        clock.tick(FPS)
        fill(Circle_small,green)
        fill(Circle, green)
        update_window(Win, Lines_color, Lines_color_2, Width, Square, Small_Square, margin, Cross_small, Circle_small, Cross, Circle, small_boards, main_board, turn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE and game_over:
                    Game_Board.reset(small_boards, main_board, game_over)
                    game_over = False

            if event.type == pygame.MOUSEBUTTONDOWN and turn == Human and not game_over:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()


                    if set_locations(small_boards, main_board, pos[0]//(Small_Square), pos[1]//(Small_Square), turn, box):
                        #print("pos",pos[0]//(Small_Square), pos[1]//(Small_Square))
                        check_game(small_boards, main_board,turn)
                        new_box = get_possible_moves(small_boards,pos[0]//(Small_Square), pos[1]//(Small_Square))
                        #print("box after get_possible_moves", new_box)
                        box = Validate_box(small_boards, main_board, new_box,pos[0]//(Small_Square), pos[1]//(Small_Square))
                        #print("Box validated", box)

                        #print("small_boards", small_boards)
                        if Check_Big_Board(main_board, turn):
                            game_over = True

                        turn = AI
        if turn == AI:
            Depth = 2
            new_Board,value, pos = Minimax(small_boards, main_board,Depth, box,turn, True)
            small_boards = new_Board
            check_game(small_boards,main_board,turn)

            new_box = get_possible_moves(small_boards,pos[0], pos[1])

            box = Validate_box(small_boards, main_board, new_box,pos[0]//(Small_Square), pos[1]//(Small_Square))


            if Check_Big_Board(main_board, turn):
                game_over = True

            turn = Human



main()
