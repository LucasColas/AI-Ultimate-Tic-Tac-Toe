from minimax_def import terminal_node, evaluate, Possibles_moves
from Check_game import empty_cells_small_boards, set_locations, valid_locations
from math import inf as infinity
import random
import copy

def random_piece(board, big_board, player):
    choice_1 = random.randrange(len(empty_cells_small_boards(board)))
    pos = empty_cells_small_boards(board)[choice_1]
    x,y = pos[0], pos[1]
    return x,y


def minimax_algo(board,big_board, depth, player, Maximizing):
    if depth <= 0 or terminal_node(board, big_board, player):
        return [evaluate(board, big_board, player), board]


    if Maximizing:
        maxEvaluation = float('-inf')
        best = None
        for move in Possibles_moves(board, main_board, player):
            evaluation = minimax(board, big_board, depth-1, -1, False)[0]
            maxEvaluation = max(maxEvaluation, evaluation)
            if maxEvaluation == evaluation:
                best = move

        return maxEvaluation, best

    else:
        minEvaluation = float('inf')
        best = None
        for move in Possibles_moves(board, main_board, player):
            evaluation = minimax(board, big_board, depth-1, -1, False)[0]
            minEvaluation = min(maxEvaluation, evaluation)
            if minEvaluation == evaluation:
                best = move

        return minEvaluation, best
