import copy
from Board import new_Board
#Récupérer les coups possibles / états
#Les évaluer. Prendre le meilleur dans le cas de max.
#Prendre le moins bon dans le cas de min

Board = new_Board()
Boards = Board.every_small_boards()
def all_moves(Board, player):
    all_moves = []
    for y, row in Board:
        for x, cell in Board:
            if cell == 0:
                new_Board = copy.deepcopy(Board)
                new_Board[y][x] = player

    return all_moves
