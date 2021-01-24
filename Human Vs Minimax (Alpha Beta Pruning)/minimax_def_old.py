from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import Check_Big_Board, set_locations
from Check_game import get_possible_moves, Validate_box
from minimax_assets import See_diagonals, See_vertically, See_horizontally
from minimax_assets import eval_small_boxes
import copy
#from Board import new_Board

#Board = new_Board()
#boards = Board.every_small_boards()


def all_moves(Board, main_board,box,player):
    all_moves = []
    all_boxes = []

    if box == None:
        for y, row in enumerate(Board):
            for x, cell in enumerate(row):
                if cell == 0:
                    new_Board = copy.deepcopy(Board)
                    new_main_board = copy.deepcopy(main_board)
                    if set_locations(new_Board, new_main_board, x,y, player,box):
                        Box = get_possible_moves(new_Board,x,y)
                        Good_Box = Validate_box(new_Board, new_main_board,Box,x,y)
                        all_moves.append(new_Board)
                        all_boxes.append(Good_Box)

        return all_moves,all_boxes

    else:
        for [x,y] in box:
            new_Board = copy.deepcopy(Board)
            new_main_board = copy.deepcopy(main_board)
            if set_locations(new_Board, new_main_board, x,y, player,box):
                Box = get_possible_moves(new_Board,x,y)
                Good_Box = Validate_box(new_Board, new_main_board,Box,x,y)
                all_moves.append(new_Board)
                all_boxes.append(Good_Box)
        return all_moves,all_boxes





"""
def all_moves(Board, main_board, player):
    all_moves = []

    for y, row in enumerate(Board):
        for x, cell in enumerate(row):
            if cell == 0:
                new_Board = copy.deepcopy(Board)
                new_main_board = copy.deepcopy(main_board)
                if set_locations(new_Board, new_main_board, x,y, player):
                    all_moves.append(new_Board)

    return all_moves
"""

#all_moves(boards,1)

def evaluate(Board, player):
    score = 0
    Gamma = 90

    #score = eval_small_boxes(Board, player) + Gamma*get_score(Board, player)
    score = eval_small_boxes(Board, player)

    return score

def terminal_state(Board, player):
    return end_game(Board, player)


def end_game(Board,player):
    total_score = get_score(Board, player)
    if total_score == 3:
        return True

    if len(empty_cells_small_boards(Board)) == 0:
        return True

def get_score(Board, player):
    score = 0

    score += See_horizontally(Board, player)

    score += See_vertically(Board, player)

    score += See_diagonals(Board, player)


    return score