from minimax_def import terminal_node, evaluate, get_moves
from Check_game import empty_cells_small_boards

from math import inf as infinity
import random
import copy

def random_piece(board, big_board, player):
    choice = random.randrange(len(get_moves(board, big_board, player)))

    new_board = get_moves(board, big_board, player)[choice]
    return new_board


def minimax_algo(node,big_board, depth, player, Go):
    if depth <= 0 or terminal_node(node, big_board, player):
        return evaluate(node), None, None

    if player == AI:
        best = [-infinity, None, None]

    for place in empty_cells_small_boards(node):
        x,y = place[0], place[1]
        node[y][x] = player
        info = minimax_algo(node, big_board, depth-1, -player, False)
        node[y][x] = 0
        info[1], info[2] == x,y

        if player == AI:
            if info[0] < evaluation[0]:
                info = evaluation

        else:
            if best[2] > info[2]:
                best = info

    return best

def minimax(node, big_board, depth, player, alpha, beta,MaximizingPlayer):
    if depth <= 0 or terminal_node(node, big_board, player):
        return evaluate(node),None
    #print("Yes")

    for each_place in empty_cells_small_boards(node):
        print("enter")
        good_node = None
        x,y = each_place[0], each_place[1]
        node[y][x] = player
        evaluation = minimax(node, big_board, depth-1,-player, alpha,beta,False)[0]

        ("each place", each_place)
        if MaximizingPlayer:

            value = -infinity
            value = max(value, evaluation)
            if value == evaluation:
                good_node = copy.deepcopy(node)
            alpha = max(alpha, value)
            if alpha >= beta:
                break

        else:
            value = +infinity
            value = min(value, evaluation)
            if value == evaluation:
                good_node = copy.deepcopy(node)

            beta = min(beta, value)
            if alpha >= beta:
                break
        node[y][x] = 0

    return value, good_node

    """
    if MaximizingPlayer:
        value = -infinity
        good_node = None
        for each_place in empty_cells_small_boards(node):
            x,y = each_place[0], each_place[1]
            node[y][x] = player
            evaluation = minimax(node, big_board, depth-1, -1,alpha, beta, False)[0]
            node[y][x] = 0
            value = max(value, evaluation)
            #print("value", value)
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
        for each_place in empty_cells_small_boards(node):
            x,y = each_place[0], each_place[1]
            node[y][x] = player
            evaluation = minimax(node, big_board, depth-1, -1,alpha, beta, False)[0]
            node[y][x] = 0
            value = min(value, evaluation)
            if value == evaluation:
                good_node = node
            beta = min(beta, value)
            if alpha >= beta:
                break

        print("good_node else", good_node)
        return value, good_node
    """
