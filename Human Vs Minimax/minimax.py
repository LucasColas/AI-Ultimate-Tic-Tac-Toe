from Check_game import empty_cells_small_boards
from Check_game import check_game, place_big_board
from copy import deepcopy

def terminal_node(board, big_board, player):

    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def minimax(node, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_node(board, big_board):
        return evaluate(node),node

    if MaximizingPlayer:
        for node in get_moves(board, player):
            evaluate = minimax(node, big_board, depth-1, -player, False)[0]

    else:
        pass

def evaluate(node):

    score = 0
    

    return score

def get_moves(board, big_board,player):
    moves = []
    for empty_cells in empty_cells_small_boards(board):
        new_board = deepcopy(board)
        x,y = empty_cells[0], empty_cells[1]
        new_board[y][x] = player
        moves.append(new_board)
        new_big_board = deepcopy(big_board)
        check_game(new_board,new_big_board, player)

    return moves
