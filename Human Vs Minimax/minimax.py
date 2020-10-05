from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import check_game, place_big_board, Check_Big_Board
from copy import deepcopy

from math import inf as infinity

def terminal_node(board, big_board, player):
    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def minimax(node, big_board, depth, player, alpha, beta,MaximizingPlayer):
    if depth <= 0 or terminal_node(node, big_board, player):
        return evaluate(),node
    depth -= 1

    if MaximizingPlayer:
        value = -infinity
        good_node = None
        for node in get_moves(node, big_board,player):
            print("node", node)
            evaluation = minimax(node, big_board, depth, -1,alpha, beta, False)[0]
            value = max(value, evaluation)
            if value == evaluation:
                good_node = node
            alpha = max(alpha, value)
            if alpha >= beta:

                break
        #print("good_node", good_node)
        return value, good_node

    else:
        value = +infinity
        good_node = None
        for node in get_moves(node,big_board,player):
            #print("node", node)
            evaluation = minimax(node, big_board, depth, 1,alpha, beta, True)[0]
            value = min(value, evaluation)
            if value == evaluation:
                good_node = node
            beta = min(beta, value)
            if alpha >= beta:
                break
        #print("good_node",good_node)
        return value, good_node



def evaluate():

    score = 0


    return score

def get_moves(board, big_board,player):
    moves = []
    big_boards = []
    for empty_cells in empty_cells_small_boards(board):

        new_board = deepcopy(board)
        new_big_board = deepcopy(big_board)
        x,y = empty_cells[0], empty_cells[1]
        if [x//3,y//3] in empty_cells_big_board(big_board):
            new_board[y][x] = player
            check_game(new_board, new_big_board, player)

            moves.append(new_board)

    return moves
