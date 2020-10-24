from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import check_game, place_big_board, Check_Big_Board, Check_empty_cells

import copy
#from math import inf as infinity

def Possibles_moves(board, player):
    for empty_cells_small_boards(board):
        pass

def terminal_node(board, big_board, player):
    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def evaluate(board, main_board, player):

    score = 15
    if check_game(board, main_board, 1):
        score = 5

    elif check_game(board, main_board, -1):
        score = -5

    elif Check_empty_cells(board):
        score = 0

    return score
