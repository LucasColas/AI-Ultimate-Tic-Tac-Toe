from minimax_def import all_moves,  evaluate, terminal_state
import copy
from math import inf as infinity


def Minimax(Board, main_board, depth, player, alpha, beta, box,MaximizingPlayer):
    if depth <= 0 or terminal_state(Board, player):
        return (evaluate(Board, player),Board)


    #print("all all_moves : ", all_moves(Board, player))

    if MaximizingPlayer:
        score = float('-inf')
        Good_B = None
        for Board_,Box_ in all_moves(Board, main_board,box, player):
            #print("Board : ", Board_)
            value = Minimax(Board_, main_board, depth-1, -player, alpha, beta, Box_, False)[0]
            #print("value", value)
            if value > score:
                score = value

            if value == score:
                Good_B = Board_
            alpha = max(alpha, value)
            if alpha >= beta:
                break
            #print("score", score)
        return score, Good_B #same type of return

    else:
        score = float('inf')
        Good_B = None
        for Board_,Box_ in all_moves(Board, main_board,box, player):
            value = Minimax(Board_, main_board, depth-1, -player, alpha, beta, Box_, True)[0]
            #print("value", value)
            #print("score", score)
            if value < score:
                score = value

            if value == score:
                Good_B = Board_

            beta = min(beta, value)
            if alpha >= beta:
                break
        return score, Good_B
