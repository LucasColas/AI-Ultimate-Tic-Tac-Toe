from Check_game import empty_cells_small_boards
from Check_game import Check_Big_Board

def minimax(node, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or Check_Big_Board(big_board):
        return evaluate(node),position

    if MaximizingPlayer:
        for move in get_moves():
            pass


def evaluate(big_board):
    score = 0
    for row in big_board:
        for x in row:
            if x == 1:
                score += 1

    return score


def get_moves():
    pass
