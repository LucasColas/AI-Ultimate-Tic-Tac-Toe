from minimax_def import all_moves,  evaluate, terminal_state
import copy
from math import inf as infinity

def Minimax(Board, main_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_state(Board, player):
        if terminal_state(Board, player):
            if terminal_state(Board, 1):
                 return (10,Board)
            if terminal_state(Board,-1):
                return (-10,Board)
            else:
                return (0, Board)
        else:
            return (evaluate(Board, player), Board)

    #print("all all_moves : ", all_moves(Board, player))

    if MaximizingPlayer:
        score = float('-inf')
        Good_B = None
        for Board_ in all_moves(Board, main_board, player):
            print("Board : ", Board_)
            value = Minimax(Board_, main_board, depth-1, -player, False)[0]
            score = max(value, score)
            if value == score:
                Good_B = Board_
        return score, Good_B #same type of return

    else:
        score = float('inf')
        Good_B = None
        for Board_ in all_moves(Board, main_board, player):
            value = Minimax(Board_, main_board, depth-1, -player, True)[0]
            #print("value", value)
            #print("score", score)
            score = min(value, score)
            if value == score:
                Good_B = Board_
        return score, Good_B
