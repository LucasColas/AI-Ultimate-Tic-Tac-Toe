from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import Check_Big_Board
from minimax_assets import See_diagonals, See_vertically, See_horizontally
import copy


def all_moves(Board, player):
    all_moves = []
    all_big_board = []
    for y, row in enumerate(Board):
        #print(row)
        for x, cell in enumerate(row):
            #print(cell)
            if cell == 0:
                new_Board = copy.deepcopy(Board)
                new_Board[y][x] = player
                #all_moves.append(new_Board)
                #new_big_board = copy.deepcopy(big_board)
                #check_game(board, new_big_board, player)
                #all_big_board.append(new_big_board)
                #print(new_Board)

    return all_moves


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
    total_score_AI, total_score_Human = See_horizontally(Board, player)
    total_score_AI, total_score_Human += See_vertically(Board, player)
    total_score_AI, total_score_Human += See_diagonals(Board, player)

    return total_score_AI, total_score_Human

def evaluate(Board, player):
    total_score_AI, total_score_Human = get_score(Board, player)
    #total_score = total_score_AI + total_score_Human

    if total_score_AI == 3:
        score = 1
        return score

    if total_score_Human == 3:
        score = -1
        return score

    if len(empty_cells_small_boards(Board)) == 0:
        score = 0
        return score
