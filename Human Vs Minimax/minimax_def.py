from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import Check_Big_Board, set_locations
from minimax_assets import See_diagonals, See_vertically, See_horizontally
from Board import new_Board
import copy

#Board = new_Board()
#boards = Board.every_small_boards()

def all_moves(Board, main_board, player):
    all_moves = []

    for y, row in enumerate(Board):

        for x, cell in enumerate(row):
            if cell == 0:
                new_Board = copy.deepcopy(Board)
                new_main_board = copy.deepcopy(main_board)
                if set_locations(new_Board, new_main_board, x,y, player):
                    all_moves.append(new_Board)

    return all_moves


#all_moves(boards,1)

def evaluate(Board, player):
    score = 0

    score += score_horizontally(Board, player)
    score += score_vertically(Board, player)
    score += score_diagonals(Board, player)

    return score

def evaluate_game(pieces, player):
    opp_piece = -1
    if player == -1:
        opp_piece = 1

    score = 0

    if pieces.count(player) == 3:
        score += 50

    if pieces.count(player) == 2 and pieces.count(0) == 1:
        score += 20

    if pieces.count(player) == 1 and pieces.count(0) == 2:
        score += 5

    if pieces.count(opp_piece) == 2 and pieces.count(0) == 1:
        score -= 8


    return score


def score_horizontally(Board,player):
    score = 0
    for inx, row in enumerate(board):
        for i in range(0,7,3):
            pieces = row[i:i+3]
            score += evaluate_game(pieces, player)

    return score

def score_vertically(Board, player):

    score = 0
    for indx in range(len(board)):
        check = []

        for i,row in enumerate(board):
            check.append(row[indx])

            if len(check) >= 3:
                score += evaluate_game(check, player)
                check.clear()

    return score


def score_diagonals(Board, player):
    score = 0
    for x in range(0,8, 3):

        stock_indx = []
        for y in range(0,8,3):

            stock_indx.append(board[y][x])
            for i in range(1,3):
                stock_indx.append(board[y+i][x+i])

                if len(stock_indx) >= 3:
                    score += evaluate_game(stock_indx, player)
                    stock_indx.clear()

    for x in range(0,9,3):
        stock_nindx = []
        for y in range(2,9,3):

            for i in range(3):
                stock_nindx.append(board[y-i][x+i])

                if len(stock_nindx) >= 3:
                    score += evaluate_game(stock_nindx, player)
                    stock_nindx.clear()

    return score

def terminal_state(Board, player):
    return end_game(Board, player)


def end_game(Board,player):
    total_score_AI, total_score_Human = get_score(Board, player)
    if total_score_AI == 3 or total_score_Human == 3 :
        return True

    if len(empty_cells_small_boards(Board)) == 0:
        return True

def get_score(Board, player):
    score_AI, score_Human = 0,0

    sc_h_AI, sc_h_H = See_horizontally(Board, player)
    score_AI += sc_h_AI
    score_Human += sc_h_H

    sc_v_AI, sc_v_H = See_vertically(Board, player)
    score_AI += sc_v_AI
    score_Human += sc_v_H

    sc_d_AI, sc_d_H = See_diagonals(Board, player)
    score_AI += sc_d_AI
    score_Human += sc_d_H

    return score_AI, score_Human
