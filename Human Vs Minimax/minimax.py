from Check_game import empty_cells_small_boards
from Check_game import Check_Big_Board

def minimax(node, depth, player, MaximizingPlayer):
    if depth == 0 or Check_Big_Board:
        return evaluate,node
