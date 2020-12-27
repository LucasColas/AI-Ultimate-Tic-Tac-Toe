def get_small_box(Board, player):
    for i in range(0,9,3):
        small_box = []
        for j in range(0,9,3):
            for h in range(3):
                for k in range(3):
                    small_box.append(Board[h+i][j+k])
            #print(small_box)
            small_box.clear()



def evaluate_small_box(Board, player):
    pass
