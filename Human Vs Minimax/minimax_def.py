
from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import check_game, place_big_board, Check_Big_Board, Check_empty_cells
from check_game import set_locations
import copy
#from math import inf as infinity

def Possibles_moves(board, main_board,player):
    small_boards = []
    big_boards = []
    for location in empty_cells_small_boards(board):
        temp_board = copy.deepcopy(board)
        temp_big_board = copy.deepcopy(main_board)
        set_locations(temp_board, temp_big_board, location[0], location[1], player)
        small_boards.append(temp_board)
        big_boards.append(temp_big_board)
    return small_boards, big_boards

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
