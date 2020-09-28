from Check_game import empty_cells_small_boards
from Check_game import Check_Big_Board

def terminal_node(board, big_board):
    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def minimax(node, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_node(board, big_board):
        return evaluate(node),position

    if MaximizingPlayer:
        for node in get_moves(board, player):
            evaluate = minimax(node, big_board, depth-1, -player, False)[0]

    else:
        pass

def evaluate(node):
    score = 0
    return score

def get_moves(board, player):
    pass
