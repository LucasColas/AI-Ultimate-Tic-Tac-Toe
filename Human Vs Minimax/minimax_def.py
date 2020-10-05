from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import check_game, place_big_board, Check_Big_Board

from copy import deepcopy
from math import inf as infinity


def terminal_node(board, big_board, player):
    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def evaluate(board):

    total_score = 0
    if len(empty_cells_small_boards(board)) == 0:
        total_score += 1



def score_horizontally(board):
    score = 0
    for i in range(0,7,3):
        for indx, row in enumerate(board):
            if row[0+i] == row[1+i] == row[2+i] == 1:
                score += 3
            if row[0+i] == row[1+i] == row[2+i] == -1:
                score -= 3

        return score

def score_vertical(board):
    for indx in range(len(board)):
        check = []
        for i,row in enumerate(board):
            check.append(row[indx])
            #print(check)
            if len(check) >= 3:
                if check.count(player) == len(check) and check[0] != 0:
                    print(player, "succeeds (vertically)")
                    good_col = True
                    if good_col:
                        place_big_board(main_board,indx//3,i//3,player)
                        good_col = False

                    else:
                        check.clear()
                else:
                    check.clear()




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
