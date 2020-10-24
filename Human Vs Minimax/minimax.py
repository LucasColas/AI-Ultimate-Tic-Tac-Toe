from minimax_def import terminal_node, evaluate
from Check_game import empty_cells_small_boards, set_locations, valid_locations
from math import inf as infinity
import random
import copy

def random_piece(board, big_board, player):
    choice_1 = random.randrange(len(empty_cells_small_boards(board)))
    pos = empty_cells_small_boards(board)[choice_1]
    x,y = pos[0], pos[1]
    return x,y

def test(board):
    for place in empty_cells_small_boards(board):
        print("place", place)

def minimax_algo(board,big_board, depth, player):
    if depth <= 0 or terminal_node(board, big_board, player):
        return [evaluate(board, big_board, player), -1, -1]

    if player == 1: #AI
        best = [-infinity, -1, -1]

    else:
        best = [+infinity, -1, -1]

    for place in empty_cells_small_boards(board):
        print("empty_cells", empty_cells_small_boards(board))
        x,y = place[0], place[1]
        print("x : ", x, "y : ", y)
        set_locations(board, big_board,x,y, player)
        info = minimax_algo(board, big_board, depth-1, -player)
        board[y][x] = 0
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

def ai_choose(board, big_board, depth, player):
    info = minimax_algo(board, big_board, depth, player)
    x,y = info[2], info[1]
    print("x,y", x,y)
    set_locations(board, big_board,x,y, player)
