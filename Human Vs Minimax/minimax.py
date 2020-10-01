from Check_game import empty_cells_small_boards
from Check_game import check_game, place_big_board, Check_Big_Board
from copy import deepcopy

from math import inf as infinity

def terminal_node(board, big_board, player):
    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def minimax(node, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_node(node, big_board, player):
        return evaluate(big_board),node

    if MaximizingPlayer:
        value = -infinity
        good_node = None
        for node in get_moves(node, big_board,player):
            evaluation = minimax(node, big_board, depth-1, -player, False)[0]
            value = max(value, evaluation)
            if value == evaluation:
                good_node = node

        return value, good_node

    else:
        value = +infinity
        good_node = None
        for node in get_moves(node,big_board,player):
            evaluation = minimax(node, big_board, depth-1, -player, True)[0]
            value = min(value, evaluation)
            if value == evaluation:
                good_node = node

        return value, good_node



def evaluate(node):

    score = 0
    for row in node:
        for value in row:
            if value == -1:
                score -= 5
            elif value == 0:
                score -= 1
            else:
                score += 5

    return score

def get_moves(board, big_board,player):
    moves = []
    big_boards = []
    for empty_cells in empty_cells_small_boards(board):
        new_board = deepcopy(board)
        x,y = empty_cells[0], empty_cells[1]
        new_board[y][x] = player
        moves.append(new_board)
        new_big_board = deepcopy(big_board)
        #print(new_board)
        check_game(new_board,new_big_board, player)
        #print("checked")
        big_boards.append(new_big_board)


    return moves
