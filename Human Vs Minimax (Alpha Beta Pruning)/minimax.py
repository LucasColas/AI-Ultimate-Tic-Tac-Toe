import copy

from Check_game import set_locations

def minimax(Board, Main_board,Depth, Box, Player,MaximizingPlayer):
    if Depth == 0:
        pass

def get_all_moves(Board, Main_board, Box, Player):
    for x,y in Box:
        new_Board = copy.deecopy(Board)
        new_Main_board = copy.deecopy(Board)
        if set_locations(new_Board, new_Main_board,x,y, player,Box):
            pass
