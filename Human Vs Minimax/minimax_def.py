from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import check_game, place_big_board, Check_Big_Board, Check_empty_cells
from Check_game import set_locations
from Board import new_Board
import copy
#from math import inf as infinity
Board = new_Board()
Boards = Board.every_small_boards()
def all_moves(Board, player):
    all_moves = []
    for y, row in Board:
        for x, cell in Board:
            if cell == 0:
                new_Board = copy.deepcopy(Board)
                new_Board[y][x] = player

    return all_moves

all_moves(Board, 1)
