from minimax_def import terminal_node, evaluate
from Check_game import empty_cells_small_boards
from Board import set_locations
from math import inf as infinity
import random
import copy

def random_piece(board, big_board, player):
    choice_1 = random.randrange(len(empty_cells_small_boards(board)))
    pos = empty_cells_small_boards(board)[choice_1]
    x,y = pos[0], pos[1]
    return x,y


def minimax_algo(node,big_board, depth, player):
    if depth <= 0 or terminal_node(node, big_board, player):
        return [evaluate(node, big_board, player), -1, -1]

    if player == 1: #AI
        best = [-infinity, -1, -1]

    else:
        best = [+infinity, -1, -1]

    for place in empty_cells_small_boards(node):
        #print("empty_cells", empty_cells_small_boards(node))
        x,y = place[0], place[1]
        #print("x : ", x, "y : ", y)
        node[y][x] = player
        info = minimax_algo(node, big_board, depth-1, -player)
        node[y][x] = 0
        info[1], info[2] = x,y
        #print("info,", info)

        if player == 1: #AI
            if info[0] > best[0]:
                print("best")
                best = info
                print("best", best)

        else:
            if best[0] > info[0]:
                best = info

    return best

def ai_turn(node, big_board,depth, player):
    if terminal_node(node, big_board, player):
        return

    if len(empty_cells_small_boards(node)) == 81:
        choice_1 = random.randrange(len(empty_cells_small_boards(board)))
        pos = empty_cells_small_boards(board)[choice_1]
        x,y = pos[0], pos[1]
    else:
        value,y,x = minimax_algo(node,big_board, depth, player)

    set_locations(board, main_board, x,y, player)
