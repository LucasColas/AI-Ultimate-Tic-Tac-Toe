from minimax_def import terminal_node, evaluate, get_moves
from math import inf as infinity
import random

def random_piece(board):
    choice = random.randrange(len(board))
    new_board = board[choice]

    return new_board

def minimax(node, big_board, depth, player, alpha, beta,MaximizingPlayer):
    if depth <= 0 or terminal_node(node, big_board, player):
        return evaluate(node),node


    if MaximizingPlayer:
        value = -infinity
        good_node = None
        for node in get_moves(node, big_board,player):
            #print("node", node)
            evaluation = minimax(node, big_board, depth-1, -1,alpha, beta, False)[0]
            value = max(value, evaluation)
            print("value", value)
            if value == evaluation:
                good_node = node
            alpha = max(alpha, value)
            if alpha >= beta:

                break
        print("good_node if", good_node)
        return value, good_node

    else:
        value = +infinity
        good_node = None
        for node in get_moves(node,big_board,player):
            #print("node", node)
            evaluation = minimax(node, big_board, depth-1, 1,alpha, beta, True)[0]
            value = min(value, evaluation)
            if value == evaluation:
                good_node = node
            beta = min(beta, value)
            if alpha >= beta:
                break
        #print("good_node",good_node)
        print("good_node else", good_node)
        return value, good_node
