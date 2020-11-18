import copy

#Récupérer les coups possibles / états
#Les évaluer. Prendre le meilleur dans le cas de max.
#Prendre le moins bon dans le cas de min

def Minimax(board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_state():
        return evaluate(board, big_board, player)

    
