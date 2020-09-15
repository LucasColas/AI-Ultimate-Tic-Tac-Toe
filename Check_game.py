
def empty_cells_small_boards(board):
    empty_cells = []
    for x,row in enumerate(board):
        for y,case in enumerate(row):
            if case == 0:
                empty_cells.append([x,y])

    return empty_cells

def empty_cells_big_board(main_board):
    empty_cells = []
    for x,row in enumerate(main_board):
        for y,case in enumerate(row):
            if case == 0:
                empty_cells.append([x,y])

    return empty_cells

def Check_horizontally(self,board, main_board, player):
    good = False
    for i in range(0,7,3):
        for indx, row in enumerate(board):
            if row[0+i] == row[1+i] == row[2+i] == player:
                print(player, "horizontal")
                good = True
                if good:
                    place_big_board(main_board,i//3,indx//3,player)
                    good = False

def Check_vertically(board,main_board, player):
    good_col = False
    for indx in range(len(board)):
        check = []
        for i,row in enumerate(board):
            check.append(row[indx])
            if len(check) == 3:
                if check.count(player) == len(check) and check[0] != 0:
                    print(player, "succeeds")
                    good_col = True
                    if good_col:
                        #print("indx : ", indx)
                        #print("i : ", i)
                        place_big_board(main_board,indx//3,i//3,player)
                        good_col = False

                    else:
                        check.clear()

def Check_diagonals(board, main_board, player):
    for x in range(0,8, 3):
        #print(x)
        stock_indx = []
        for y in range(0,8,3):
            print(x,y)
            stock_indx.append(board[y][x])
            for i in range(1,3):
                stock_indx.append(board[y+i][x+i])
                print("x+i : ", x+i, "y+i :", y+i)
                if len(stock_indx) >= 3:

                    if stock_indx.count(player) == len(stock_indx):
                        print(player, "succeeds")
                        place_big_board(main_board, x//3, y//3, player)
                        stock_indx.clear()

                    else:
                        stock_indx.clear()

def Check_empty_cells(board):
    if len(empty_cells_small_boards(board)) == 0:
        print("No one wins")


def Check_Big_Board(main_board, player):

    for row in main_board:
        row_stock = []
        for i in range(len(main_board)):
            row_stock.append(row[i])
            if row_stock.count(player) == len(row_stock):
                print(player, "Wins the match")
                return True

    for col in range(len(main_board)):
        col_stock = []
        for row in main_board:
            col_stock.append(row[col])
            if col_stock.count(player) == len(col_stock):
                print(player, "Wins the match")
                return True

    diag_1 = []
    for indx in range(len(main_board)):
        diag_1.append(main_board[indx][indx])
    if len(diag_1) == diag_1.count(player):
        print(player, "Wins the Match")
        return True


    diag_2 = []
    for indx, rev_indx in enumerate(reversed(range(len(main_board)))):
        diag_2.append(main_board[indx][rev_indx])
    if diag_2.count(player) == len(diag_2):
        print(player, "Wins the Match")
        return True


    if len(empty_cells_big_board(main_board)) == 0:
        print("No One Wins")
        return True
