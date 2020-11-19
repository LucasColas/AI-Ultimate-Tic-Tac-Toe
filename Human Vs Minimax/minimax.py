from minimax_def import all_moves,  evaluate, terminal_state
import copy
from math import inf as infinity

#Récupérer les coups possibles / états
#Les évaluer. Prendre le meilleur dans le cas de max.
#Prendre le moins bon dans le cas de min

def Minimax(Board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_state(Board, player):
        return evaluate(Board, player), Board

    if MaximizingPlayer:
        score = -infinity
        for Board_ in all_moves(Board, player):
            value = evaluate(Board_, depth-1, -player, False)[0]
            score = max(value, score)
        return score

    else:
        score = infinity
        for Board_ in all_moves(Board, player):
            value = evaluate(Board_, depth-1, -player, False)[0]
            score = min(value, score)
        return score
