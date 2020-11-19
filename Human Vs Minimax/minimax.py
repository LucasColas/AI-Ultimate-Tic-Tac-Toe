from minimax_def import all_moves,  evaluate, terminal_state
import copy

#Récupérer les coups possibles / états
#Les évaluer. Prendre le meilleur dans le cas de max.
#Prendre le moins bon dans le cas de min

def Minimax(Board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_state(Board, player):
        return evaluate(Board, player)
