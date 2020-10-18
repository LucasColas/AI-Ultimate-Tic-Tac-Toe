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

    else:
        best = [infinity, None, None]

    for place in empty_cells_small_boards(node):
        x,y = place[0], place[1]
        node[y][x] = player
        info = minimax_algo(node, big_board, depth-1, -player, False)
        node[y][x] = 0
        info[1], info[2] == x,y

        if player == AI:
            if info[0] > best[0]:
                info = best

        else:
            if best[2] > info[2]:
                best = info

    return best
