def opponent(player):
    return -1 if player == 1 else 1

def evaluate_game(pieces, player):

    score = 0

    three = 3*player
    two = 2*player
    one = 1*player

    three_opp = 3*opponent(player)
    two_opp = 2*opponent(player)
    one_opp = opponent(player)

    for el in pieces:
        pass 


    return score

def score_horizontally(Board,player):
    score = 0
    for inx, row in enumerate(Board):
        for i in range(0,7,3):
            pieces = row[i:i+3]
            get_score = evaluate_game(pieces, player)
            if score < get_score:
                score = get_score
    return score

def score_vertically(Board, player):

    score = 0
    for indx in range(len(Board)):
        check = []

        for i,row in enumerate(Board):
            check.append(row[indx])

            if len(check) >= 3:
                get_score = evaluate_game(check, player)
                if score < get_score:
                    score = get_score
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
                    get_score = evaluate_game(stock_indx, player)
                    if score < get_score:
                        score = get_score
                    stock_indx.clear()

    for x in range(0,9,3):
        stock_nindx = []
        for y in range(2,9,3):

            for i in range(3):
                stock_nindx.append(Board[y-i][x+i])

                if len(stock_nindx) >= 3:
                    get_score = evaluate_game(stock_nindx, player)
                    if score < get_score:
                        score = get_score
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
