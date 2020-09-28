from Check_game import empty_cells_small_boards
from Check_game import Check_Big_Board

def terminal_node(board, big_board):
    return empty_cells_small_boards(board) or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

"""
To do :
-calculate the score of a Board (each time there are a piece in the big board : +1 or -1) :
    *
-get a new board for a move
-stock those boards

"""

def minimax(node, board, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_node(board, big_board):
        return evaluate(node),position

    if MaximizingPlayer:
        for node in empty_cells_small_boards(board):
            evaluate = minimax(node, board, big_board, depth, -player, False)[0]

    else:
        pass

def evaluate(node):
    score = 0
    return score
