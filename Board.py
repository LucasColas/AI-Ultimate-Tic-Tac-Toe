

class new_Board():
    def __init__(self):
        self.hi = "hello"

    def create_board(self):
        return [[0 for x in range(3)] for y in range(3)]

    def every_small_boards(self):
        return [[0 for y in range(9)] for z in range(9)]

    def test(self):
        print(self.hi)
