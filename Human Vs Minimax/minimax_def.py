from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import check_game, place_big_board, Check_Big_Board

import copy
#from math import inf as infinity


def terminal_node(board, big_board, player):
    return len(empty_cells_small_boards(board)) == 0 or Check_Big_Board(big_board, 1) or Check_Big_Board(big_board, -1)

def evaluate(board, main_board, 1):

    score = 0

    if check_game(board, main_board, 1):
        score += 5

    elif check_game(board, main_board, -1):
        score -= 5

    elif Check_empty_cells(board):
        score += 1

    return score

"""
def score_horizontally(board):
    score = 0
    for i in range(0,7,3):
        for indx, row in enumerate(board):
            if row[0+i] == row[1+i] == row[2+i] == 1:
                score += 3
                print("score", score)
            if row[0+i] == row[1+i] == row[2+i] == -1:
                score -= 3
                print("score", score)

    return score

def score_vertical(board):
    score = 0
    for indx in range(len(board)):
        check = []
        for i,row in enumerate(board):
            check.append(row[indx])
            #print(check)
            if len(check) >= 3:
                if check.count(1) == len(check) and check[0] != 0:
                    score += 3
                    print("score", score)

                if check.count(-1) == len(check) and check[0] != 0:
                    score -= 3
                    print("score", score)

                check.clear()

    return score

def score_diagonals(board):
    score = 0
    for x in range(0,8, 3):

        stock_indx = []
        for y in range(0,8,3):
            stock_indx.append(board[y][x])
            for i in range(1,3):
                stock_indx.append(board[y+i][x+i])
                if len(stock_indx) >= 3:
                    if stock_indx.count(1) == len(stock_indx):
                        score += 3
                        stock_indx.clear()
                    if stock_indx.count(-1) == len(stock_indx):
                        score -= 3

                    else:
                        stock_indx.clear()

    for x in range(0,9,3):
        stock_nindx = []
        for y in range(2,9,3):
            for i in range(3):
                stock_nindx.append(board[y-i][x+i])

                if len(stock_nindx) >= 3:

                    if stock_nindx.count(1) == len(stock_nindx):
                        score += 3
                        stock_nindx.clear()

                    if stock_nindx.count(-1) == len(stock_nindx):
                        score -= 3
                        stock_nindx.clear()
                    else:
                        stock_nindx.clear()

    return score

def get_moves(board, big_board,player):
    moves = []
    big_boards = []
    for empty_cells in empty_cells_small_boards(board):
        #print("empty_cells", empty_cells)
        new_board = copy.deepcopy(board)
        new_big_board = copy.deepcopy(big_board)
        x,y = empty_cells[0], empty_cells[1]
        #print(x//3,y//3)
        #if [x//3,y//3] in empty_cells_big_board(big_board):
        new_board[y][x] = player

        check_game(new_board, new_big_board, player)
        #print("new board", new_board)
        #print(new_board[y][x])
        moves.append(new_board)

    return moves

"""
