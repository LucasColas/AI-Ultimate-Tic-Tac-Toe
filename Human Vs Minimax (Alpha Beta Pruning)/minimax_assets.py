

def get_small_box(Board, player):
    for i in range(0,9,3):
        small_box = []
        for j in range(0,9,3):
            for h in range(3):
                for k in range(3):
                    small_box.append(Board[h+i][j+k])
            #print(small_box)
            evaluate_small_box(small_box, player):
            small_box.clear()

def count(array, player):
    score = 0
    opp_player = -player

    if array.count(player) == 3:
        score += 100

    if array.count(player) == 2:
        score += 50

    if array.count(player) == 1:
        score += 10

    if array.count(opp_player) == 3:
        score -= 100

    if array.count(opp_player) == 2:
        score -= 50

    if array.count(opp_player) == 1:
        score -= 10

    if array.count(player) == 1 and array.count(opp_player) == 2 :
        score += 20


    return score

def evaluate_small_box(small_box, player):


    score = 0

    for row in small_box:
        score += count(row,player)

    for col in range(len(small_box)):
        check = []
        for row in small_box:
            check.append(row[col])

        score += count(col, player)

    diags = []
    for indx in range(len(board)):
        diags.append(board[indx][indx])

    score += count(diags, player)

    diags_2 = []
    for indx, rev_indx in enumerate(reversed(range(len(board)))):
        diags_2.append(board[indx][rev_indx])
    score += count(diags_2)

    if len(empty_cells(board)) == 0:
        print("No winner")
        return True
