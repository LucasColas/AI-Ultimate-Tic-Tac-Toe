import pygame


class new_Board():
    def __init__(self):
        self.hi = "hello"

    def create_board(self):
        return [[0 for x in range(3)] for y in range(3)]

    def every_small_boards(self):
        return [[[0 for x in range(3)] for y in range(3)] for z in range(3)]

    def draw_board(self, Win, Lines_color, Width, Square):
        Height = Width
        for x in range(1,9):
            pygame.draw.line(Win, Lines_color, (0, Square),(Width, Square*x) ,1)


        for i in range(1,3): #Draw horizontal lines
            pygame.draw.line(Win, Lines_color, (0, Width*(i/3)), (Width, Width*(i/3)), 1)

        for j in range(1,3):
            pygame.draw.line(Win, Lines_color, (Width*(j/3), 0), (Width*(j/3), Height), 1)





    def test(self):
        print(self.hi)
