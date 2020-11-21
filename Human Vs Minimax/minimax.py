from minimax_def import all_moves,  evaluate, terminal_state
import copy
from math import inf as infinity

def Minimax(Board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_state(Board, player):
        return evaluate(Board, player), Board #return a score and a board

    if MaximizingPlayer:
        score = -infinity
        Good_B = None
        for Board_ in all_moves(Board, player):
            value = evaluate(Board_, depth-1, -player, False)[0]
            score = max(value, score)
            if value == score:
                Good_B = Board_
        return score, Good_B #same type of return

    else:
        score = infinity
        Good_B = None
        for Board_ in all_moves(Board, player):
            value = evaluate(Board_, depth-1, -player, False)[0]
            score = min(value, score)
            if value == score:
                Good_B = Board_
        return score, Good_B
