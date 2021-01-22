from Check_game import get_possible_moves, Validate_box
from Check_game import set_locations
import copy

def minimax(Board, Main_board,Depth, Box, Player,MaximizingPlayer):
    if Depth == 0:
        pass
        
    if MaximizingPlayer:
        for Board_, Box_ in zip(get_all_moves(Board,Main_board, Box, Player)[0], get_all_moves(Board,Main_board, Box, Player)[1]):
            pass

def get_all_moves(Board, Main_board, Box, Player):
    all_Boards = []
    all_Boxes = []
    for [x,y] in Box:
        new_Board = copy.deecopy(Board)
        new_Main_board = copy.deecopy(Board)
        if set_locations(new_Board, new_Main_board,x,y, player,Box):
            Box = get_possible_moves(new_Board,x,y)
            Good_Box = Validate_box(new_Board, new_Main_board,Box,x,y)
            all_Boards.append(new_Board)
            all_Boxes.append()
    return all_Boards, all_Boxes
