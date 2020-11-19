from Check_game import empty_cells_small_boards, empty_cells_big_board
from Check_game import Check_Big_Board

#from Board import new_Board
import copy

#Board = new_Board()
#Boards = Board.every_small_boards()
#print(Boards)
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

#print(all_moves(Boards, 1))
def terminal_state(board, big_board):
    return end_game(board, big_board, player)

def end_game(board, big_board,player)

def evaluate(Board):
    score = 0

    if len(empty_cells_small_boards(Board)) == 0:
        score += 0
        return score

    return score
