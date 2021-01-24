from Check_game import get_possible_moves, Validate_box
from Check_game import set_locations
from Check_game import empty_cells_small_boards, empty_cells_big_board, Check_Big_Board
import copy

def minimax(Board, Main_board,Depth, Box, Player,MaximizingPlayer):
    if Depth == 0 or is_terminal(Board, Main_board, Player) :
        return Board, evaluate() #Function to define

    if MaximizingPlayer:
        MaxValue = float('-inf')
        Best_Board = None
        for Board_,Main_board_, Box_ in zip(get_all_moves(Board,Main_board, Box, Player)[0], get_all_moves(Board,Main_board, Box, Player)[1]):
            value = minimax(Board_,Main_board_,Depth-1, Box_,-Player, False)[1]
            MaxValue = max(MaxValue,value)
            if MaxValue == value:
                Best_Board = Board_
        return Best_Board, MaxValue

    else:
        MinValue = float('inf')
        Best_Board = None
        for Board_, Main_board_,Box_ in zip(get_all_moves(Board,Main_board, Box, Player)[0], get_all_moves(Board,Main_board, Box, Player)[1]):
            value = minimax(Board_,Main_board_,Depth-1, Box_,-Player, True)[1]
            MinValue = min(MinValue, value)
            if MinValue == value:
                Best_Board = Board_
        return Best_Board, MinValue

def evaluate():
    pass

def get_each_box(Board):
    for i in range(0,9,3):
        box = []
        for j in range(0,9,3):
            for h in range(3):
                temp_list = []
                for k in range(3):
                    temp_list.append(Board[h+i][j+k])
                box.append(temp_list)
            eval_box(box)
            box.clear()

def eval_box(box):
    score = 0
    #print("small_box", small_box)

    for row in small_box:
        #print("row", row)
        score += count_score(row,player)

    for col in range(len(small_box)):
        check = []
        for row in small_box:
            check.append(small_box[col])

        score += count_score(small_box, player)

    diags = []
    for indx in range(len(small_box)):
        diags.append(small_box[indx][indx])

    score += count_score(diags, player)

    diags_2 = []
    for indx, rev_indx in enumerate(reversed(range(len(small_box)))):
        diags_2.append(small_box[indx][rev_indx])
    score += count_score(diags_2, player)

    if len(empty_cells_small_boards(small_box)) == 0:
        score += 5


    return score

def count_score(array, player):
    opp_player = -player

def get_all_moves(Board, Main_board, Box, Player):
    all_Boards = []
    all_Big_Boards = []
    all_Boxes = []
    for [x,y] in Box:
        new_Board = copy.deecopy(Board)
        new_Main_board = copy.deecopy(Board)
        if set_locations(new_Board, new_Main_board,x,y, player,Box):
            Box = get_possible_moves(new_Board,x,y)
            Good_Box = Validate_box(new_Board, new_Main_board,Box,x,y)
            all_Boards.append(new_Board)
            all_Big_Boards.append(new_Main_board)
            all_Boxes.append(Good_Box)
    return all_Boards,all_Big_Boards, all_Boxes


def is_terminal(Board, Main_board,Player):
    if len(empty_cells_small_boards(Board)) == 0:
        return True

    if len(empty_cells_big_board(Main_board)) == 0:
        return True

    if Check_Big_Board(Main_board, Pllayer):
        return True
