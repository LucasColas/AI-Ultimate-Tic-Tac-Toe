from Check_game import empty_cells_small_boards

def eval_small_boxes(Board, player):
    score = 0
    for i in range(0,9,3):
        small_box = []
        for j in range(0,9,3):
            for h in range(3):
                temp_list = []
                for k in range(3):
                    temp_list.append(Board[h+i][j+k])
                small_box.append(temp_list)

            score += evaluate_small_box(small_box, player)
            small_box.clear()

    return score

def count(array, player):
    score = 0
    opp_player = -player

    if array.count(player) == 3:
        score += 45

    if array.count(player) == 2:
        score += 30

    if array.count(player) == 1:
        score += 1

    if array.count(opp_player) == 3:
        score -= 45

    if array.count(opp_player) == 2:
        score -= 30

    if array.count(opp_player) == 1:
        score -= 1

    if array.count(player) == 1 and array.count(opp_player) == 2 :
        score += 5

    if array.count(player) == 2 and array.count(opp_player) == 1:
        score += 15


    return score

def evaluate_small_box(small_box, player):

    score = 0
    #print("small_box", small_box)

    for row in small_box:
        #print("row", row)
        score += count(row,player)

    for col in range(len(small_box)):
        check = []
        for row in small_box:
            check.append(small_box[col])

        score += count(small_box, player)

    diags = []
    for indx in range(len(small_box)):
        diags.append(small_box[indx][indx])

    score += count(diags, player)

    diags_2 = []
    for indx, rev_indx in enumerate(reversed(range(len(small_box)))):
        diags_2.append(small_box[indx][rev_indx])
    score += count(diags_2, player)

    if len(empty_cells_small_boards(small_box)) == 0:
        score += 5


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
