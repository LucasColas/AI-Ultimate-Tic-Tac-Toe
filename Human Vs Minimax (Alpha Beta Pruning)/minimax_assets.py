def get_small_box(Board, player):
    for i in range(0,9,3):
        small_box = []
        for j in range(0,9,3):
            for h in range(3):
                for k in range(3):
                    small_box.append(Board[j][h+k])


def evaluate_small_box(Board, player):
    pass
