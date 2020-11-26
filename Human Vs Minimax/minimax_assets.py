

def See_horizontally(board, player):
    good = False
    score_AI = 0
    score_Human = 0
    for i in range(0,7,3):
        for indx, row in enumerate(board):
            if row[0+i] == row[1+i] == row[2+i] == player:
                print(player, "horizontal")
                good = True
                if good:

                    if player == 1:
                        score_AI += 1
                    else:
                        score_Human += 1
                    good = False
    return score_AI, score_Human

def See_vertically(board, player):
    good_col = False
    score_AI = 0
    score_Human = 0
    for indx in range(len(board)):
        check = []
        for i,row in enumerate(board):
            check.append(row[indx])
            #print(check)
            if len(check) >= 3:
                if check.count(player) == len(check) and check[0] != 0:

                    good_col = True
                    if good_col:
                        if player == 1:
                            score_AI += 1
                        else:
                            score_Human += 1

                        good_col = False


                    else:
                        check.clear()
                else:
                    check.clear()

    return score_AI, score_Human

def See_diagonals(board, player):
    score_AI = 0
    score_Human = 0
    for x in range(0,8, 3):

        stock_indx = []
        for y in range(0,8,3):

            stock_indx.append(board[y][x])
            for i in range(1,3):
                stock_indx.append(board[y+i][x+i])

                if len(stock_indx) >= 3:
                    if stock_indx.count(player) == len(stock_indx):

                        if player == 1:
                            score_AI += 1
                        else:
                            score_Human += 1
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

                        if player == 1:
                            score_AI += 1
                        else:
                            score_Human += 1
                        stock_nindx.clear()


                    else:
                        stock_nindx.clear()

    return score_AI, score_Human
