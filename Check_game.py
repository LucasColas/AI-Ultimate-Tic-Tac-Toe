
class Check():

    def __init__(self):
        self.test = "test"

    def Check_horizontally(self,board, main_board, player):
        for i in range(0,7,3):
            for indx, row in enumerate(board):
                if row[0+i] == row[1+i] == row[2+i] == player:
                    print(player, "horizontal")
                    good = True
                    if good:
                        place_big_board(main_board,i//3,indx//3,player)
                        good = False

    def Check_vertically(board,main_board, player):
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

                        else:
                            check.clear()
