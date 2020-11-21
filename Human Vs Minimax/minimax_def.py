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
def terminal_state(board, player):
    return end_game(board, player)

def end_game(board,player):
    total_score = evaluate(Board, player)
    if total_score == 3: #ToModify
        return True

    if len(empty_cells_small_boards(Board)) == 0:
        return True


def evaluate(Board, player):
    score = 0
    score += See_horizontally(Board, player)
    score += See_vertically(Board, player)
    score += See_horizontally(Board, player)

    if len(empty_cells_small_boards(Board)) == 0:
        score += 0
        return score

    return score

def See_horizontally(board, main_board, player):
    good = False
    score = 0
    for i in range(0,7,3):
        for indx, row in enumerate(board):
            if row[0+i] == row[1+i] == row[2+i] == player:
                print(player, "horizontal")
                good = True
                if good:
                    #place_big_board(main_board,i//3,indx//3,player)
                    score +=1
                    good = False
    return score



def See_vertically(board, player):
    good_col = False
    score = 0
    for indx in range(len(board)):
        check = []
        for i,row in enumerate(board):
            check.append(row[indx])
            #print(check)
            if len(check) >= 3:
                if check.count(player) == len(check) and check[0] != 0:

                    good_col = True
                    if good_col:
                        score += 1

                        good_col = False


                    else:
                        check.clear()
                else:
                    check.clear()

    return score

def See_diagonals(board, main_board, player):
    score = 0
    for x in range(0,8, 3):

        stock_indx = []
        for y in range(0,8,3):

            stock_indx.append(board[y][x])
            for i in range(1,3):
                stock_indx.append(board[y+i][x+i])

                if len(stock_indx) >= 3:
                    if stock_indx.count(player) == len(stock_indx):
                        #a,b = y+i, x+i
                        #print(player, "succeeds with a negative diagonal")

                        stock_indx.clear()
                        score += 1



                    else:

                        stock_indx.clear()

    for x in range(0,9,3):
        stock_nindx = []
        for y in range(2,9,3):

            for i in range(3):
                stock_nindx.append(board[y-i][x+i])

                if len(stock_nindx) >= 3:

                    if stock_nindx.count(player) == len(stock_nindx):
                        #a,b = y-i, x+i
                        #print(player, "succeeds with a negative diagonal")
                        score +=1
                        stock_nindx.clear()


                    else:
                        stock_nindx.clear()
    return score
