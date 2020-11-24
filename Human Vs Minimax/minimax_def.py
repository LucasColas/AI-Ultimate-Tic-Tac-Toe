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
def evaluate_game(pieces, player):
    opp_piece = -1
    if player == -1:
        opp_piece = 1

    score = 0

    if pieces.count(player) == 3:
        score += 50

    if pieces.count(player) == 2 and pieces.count(0) == 1:
        score += 20
        
    if pieces.count(player) == 1 and pieces.count(0) ==2:
        score += 5

    if pieces.count(opp_piece) == 2:
        score -= 8






def terminal_state(Board, player):
    return end_game(Board, player)











def end_game(Board,player):
    total_score_AI, total_score_Human = get_score(Board, player)
    if total_score_AI == 3 or total_score_Human == 3 :
        return True

    if len(empty_cells_small_boards(Board)) == 0:
        return True

def get_score(Board, player):

    total_score_AI = 0
    total_score_Human = 0

    sh_AI, sh_H = See_horizontally(Board, player)
    total_score_AI += sh_AI
    total_score_Human += sh_H

    sv_AI, sv_H = See_vertically(Board, player)
    total_score_AI += sv_AI
    total_score_Human += sv_H

    sd_AI, sd_H = See_diagonals(Board, player)
    total_score_AI += sd_AI
    total_score_Human += sd_H

    return total_score_AI, total_score_Human

def evaluate(Board, player):
    total_score_AI, total_score_Human = get_score(Board, player)

    score = 0
    if total_score_AI == 3:
        score = 1
        return score

    if total_score_Human == 3:
        score = -1
        return score

    if len(empty_cells_small_boards(Board)) == 0:
        score = 0
        return score

    return score
