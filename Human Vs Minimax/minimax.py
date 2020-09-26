from Check_game import empty_cells_small_boards
from Check_game import Check_Big_Board

def terminal_node(board, big_board):
    return empty_cells_small_boards(board) or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

"""
To do :
-calculate the score of a Board (each time there are a piece in the big board : +1 or -1) :
    *
-get a new board for a move
-stock those boards

"""

def minimax(node, board, big_board, depth, player, MaximizingPlayer):
    if depth == 0 or terminal_node(board, big_board):
        return evaluate(node),position

    if MaximizingPlayer:
        for node in get_moves():
            evaluate = minimax(node, board, big_board, depth, -player, False)[0]

    else:
        pass

def evaluate(big_board):
    score = 0
    for row in big_board:
        for x in row:
            if x == 1:
                score += 1

    return score

def get_moves():
    moves = []
    for empty_cell in empty_cells_small_boards(board):
        new_board = board.copy()
        x,y = empty_cell[0], empty_cell[1]
        new_board[y][x] = player
        moves.append(new_board)

    return moves
