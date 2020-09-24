from Check_game import empty_cells_small_boards
from Check_game import Check_Big_Board

def terminal_node(board, big_board):
    return empty_cells_small_boards(board) or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def minimax(node, board, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_node(board, big_board):
        return evaluate(node),position

    if MaximizingPlayer:
        for node in empty_cells_small_boards(board):
            pass

    else:
        pass



def evaluate(big_board):
    score = 0
    for row in big_board:
        for x in row:
            if x == 1:
                score += 1

    return score
