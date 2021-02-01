from Check_game import get_possible_moves, Validate_box, is_empty_box
from Check_game import set_locations
from Check_game import empty_cells_small_boards, empty_cells_big_board, Check_Big_Board
import copy

def Minimax(Board, Main_board,Depth, Box, Player,MaximizingPlayer):
    if Depth == 0 or is_terminal(Board, Main_board, Box,Player):
        print("in end")
        print("Depth", Depth)
        print("is_terminal",is_terminal(Board, Main_board, Box,Player))
        return Board, evaluate(Board, Player), None

    if MaximizingPlayer:
        MaxValue = float('-inf')
        Best_Board = None
        pos = None
        all_Boards,all_Big_Boards,all_Boxes,positions = get_all_moves(Board,Main_board, Box, Player)

        for Board_,Main_board_, Box_,pos_ in zip(all_Boards,all_Big_Boards,all_Boxes,positions):
            value = Minimax(Board_,Main_board_,Depth-1, Box_,-Player, False)[1]
            print("value", value)
            MaxValue = max(MaxValue,value)
            if MaxValue == value:
                Best_Board = Board_
                pos = pos_
                print("pos", pos)
        return Best_Board, MaxValue,pos

    else:
        MinValue = float('inf')
        Best_Board = None
        pos = None
        all_Boards,all_Big_Boards,all_Boxes,positions = get_all_moves(Board,Main_board, Box, Player)

        for Board_, Main_board_,Box_,pos_ in zip(all_Boards,all_Big_Boards,all_Boxes,positions):
            value = Minimax(Board_,Main_board_,Depth-1, Box_,-Player, True)[1]
            print("value", value)
            MinValue = min(MinValue, value)
            if MinValue == value:
                Best_Board = Board_
                pos = pos_
                print("pos", pos)
        return Best_Board, MinValue,pos

def evaluate(Board,player):
    score = get_score(Board,player)
    return score

def get_score(Board,player):
    score = 0
    for i in range(0,9,3):
        box = []
        for j in range(0,9,3):
            for h in range(3):
                temp_list = []
                for k in range(3):
                    temp_list.append(Board[h+i][j+k])
                box.append(temp_list)
            score += eval_box(box,player)
            box.clear()
    return score

def eval_box(box,player):
    score = 0
    #print("small_box", small_box)

    for row in box: #Score for each row
        #print("row", row)
        score += count_score(row,player)

    for col in range(len(box)): #Score for each column
        check = []
        for row in box:
            check.append(box[col])

        score += count_score(box, player)

    #A score for each diagonal
    diags = []
    for indx in range(len(box)):
        diags.append(box[indx][indx])

    score += count_score(diags, player)

    diags_2 = []
    for indx, rev_indx in enumerate(reversed(range(len(box)))):
        diags_2.append(box[indx][rev_indx])
    score += count_score(diags_2, player)

    if len(empty_cells_small_boards(box)) == 0:
        score += 1


    return score

def count_score(array, player):
    opp_player = -player
    score = 0

    if array.count(player) == 3:
        score += 100

    elif array.count(player) == 2:
        score += 50

    elif array.count(player) == 1:
        score += 20

    if array.count(opp_player) == 3:
        score -= 100

    elif array.count(opp_player) == 2:
        score -= 50

    if array.count(player) == 1 and array.count(opp_player) == 2:
        score += 10

    return score

def get_all_moves(Board, Main_board, Box, Player):
    all_Boards = []
    all_Big_Boards = []
    all_Boxes = []
    all_pos = []
    if Box == None:
        print("Box = None")
        for indx, pos in enumerate(empty_cells_small_boards(Board)):
            print(pos)
            new_Board = copy.deepcopy(Board)
            new_Main_Board = copy.deepcopy(Main_board)
            print("Box none, new_Board", new_Board)
            x = pos[0]
            y = pos[1]

            if set_locations(new_Board,new_Main_Board,x,y,Player,Box):
                print("Box none, in set_locations")
                all_Boards.append(new_Board)
                print("all_Boards", all_Boards)
                all_Big_Boards.append(new_Main_Board)
                print("all_Big_Boards", all_Big_Boards)
                Box_ = get_possible_moves(new_Board,x,y)
                new_box = Validate_box(new_Board,new_Main_Board,Box_,x,y)
                print("Box none, new_box", new_box)
                all_Boxes.append(new_box)
                print("Box none,all_Boxes",all_Boxes)
                print("pos", pos)
                all_pos.append(pos)
                print("all_pos",all_pos)
                
        return all_Boards, all_Big_Boards,all_Boxes,all_pos

    else:
        print("Box != None")
        for indx,pos in enumerate(Box):
            print(pos)
            new_Board = copy.deepcopy(Board)
            new_Main_Board = copy.deepcopy(Main_board)
            print("new_Main_Board", new_Main_Board)
            x = pos[0]
            y = pos[1]

            if set_locations(new_Board,new_Main_Board,x,y,Player,Box):
                print("yes good place")
                all_Boards.append(new_Board)
                print("all_Boards", all_Boards)
                all_Big_Boards.append(new_Main_Board)
                print("all_Big_Boards", all_Big_Boards)
                Box_ = get_possible_moves(new_Board,x, y)
                new_box = Validate_box(new_Board, new_Main_Board,Box_,x,y)
                print("new box",new_box)
                all_Boxes.append(new_box)
                print("all_Boxes",all_Boxes)
                print("pos",pos)
                all_pos.append(pos)
                print("all_pos",all_pos)


        print(all_Boards)
        return all_Boards,all_Big_Boards,all_Boxes,all_pos




def is_terminal(Board, Main_board,Box,Player):
    if len(empty_cells_small_boards(Board)) == 0:
        print("empty_cells_small_boards")
        return True

    if len(empty_cells_big_board(Main_board)) == 0:
        print("empty_cells_big_board")
        return True

    if Check_Big_Board(Main_board, Player):
        print("Big Board true")
        return True

    """
    if not is_empty_box(Board, Main_board, Box):
        print("empty box true")
        return True

    """
