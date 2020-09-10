

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

    diag_1 = []
    good_diag = False
    for indx in range(len(board)):
        diags_1s.append(board[indx][indx])
        if len(diag_1) == 3:
            if diag_1.count(player) == len(diag_1):
                print(player, "succeeds")
                good_diag = True

                if good_diag:
                    place_big_board(main_board, indx//3, indx//3, player)

                else:
                    diag_1.clear()
