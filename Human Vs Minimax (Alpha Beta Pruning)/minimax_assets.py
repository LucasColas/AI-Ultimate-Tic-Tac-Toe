
def evaluate_game(pieces, player):
    opp_player = -1
    if player == -1:
        opp_player = 1

    score = 0

    if pieces.count(player) == 3:
        score += 50

    elif pieces.count(player) == 2 and pieces.count(-1) == 1:
        score += 10

    elif pieces.count(player) == 1 and pieces.count(-1) == 1:
        score += 5

    if pieces.count(opp_player) == 2 and pieces.count(-1) == 1:
        score -= 8

    return score

def score_horizontally(Board,player):
    score = 0
    for inx, row in enumerate(Board):
        for i in range(0,7,3):
            pieces = row[i:i+3]
            score += evaluate_game(pieces, player)

    return score

def score_vertically(Board, player):

    score = 0
    for indx in range(len(Board)):
        check = []

        for i,row in enumerate(Board):
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

            stock_indx.append(Board[y][x])
            for i in range(1,3):
                stock_indx.append(Board[y+i][x+i])

                if len(stock_indx) >= 3:
                    score += evaluate_game(stock_indx, player)
                    stock_indx.clear()

    for x in range(0,9,3):
        stock_nindx = []
        for y in range(2,9,3):

            for i in range(3):
                stock_nindx.append(Board[y-i][x+i])

                if len(stock_nindx) >= 3:
                    score += evaluate_game(stock_nindx, player)
                    stock_nindx.clear()

    return score

def See_horizontally(Board, player):
    good = False
    score = 0
    for i in range(0,7,3):
        for indx, row in enumerate(Board):
            if row[0+i] == row[1+i] == row[2+i] == player:
                #print(player, "horizontal")
                good = True

                if good:
                    score += 1
                    good = False
    return score

def See_vertically(Board, player):
    good_col = False
    score = 0
    for indx in range(len(Board)):
        check = []
        for i,row in enumerate(Board):
            check.append(row[indx])
            #print(check)
            if len(check) >= 3:
                if check.count(player) == len(check) and check[0] != 0:

                    good_col = True
                    if good_col:
                        score += 1
                        good_col = False


                check.clear()

    return score

def See_diagonals(Board, player):
    score = 0
    for x in range(0,8, 3):

        stock_indx = []
        for y in range(0,8,3):

            stock_indx.append(Board[y][x])
            for i in range(1,3):
                stock_indx.append(Board[y+i][x+i])

                if len(stock_indx) >= 3:
                    if stock_indx.count(player) == len(stock_indx):

                        score += 1
                        stock_indx.clear()
                    else:

                        stock_indx.clear()

    for x in range(0,9,3):
        stock_nindx = []
        for y in range(2,9,3):

            for i in range(3):
                stock_nindx.append(Board[y-i][x+i])

                if len(stock_nindx) >= 3:

                    if stock_nindx.count(player) == len(stock_nindx):

                        score += 1
                        stock_nindx.clear()


                    else:
                        stock_nindx.clear()

    return score
