import pygame


class new_Board():
    def __init__(self):
        self.hi = "hello"

    def create_board(self):
        return [[0 for x in range(3)] for y in range(3)]

    def every_small_boards(self):
        return [[[0 for x in range(3)] for y in range(3)] for z in range(3)]

    def draw_board(self, Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin):
        Height = Width

        for x in range(1,3):
            pygame.draw.line(Win, Lines_color, (margin, ((x*Small_Square))), (Square-margin,((x*Small_Square))), 1)


        for i in range(1,3): #Draw horizontal lines
            pygame.draw.line(Win, Lines_color, (0, Square*i), (Width, Square*i), 2)

        for j in range(1,3): #Draw vertical lines
            pygame.draw.line(Win, Lines_color, (Square*j, 0), (Square*j, Height), 2)





    def test(self):
        print(self.hi)
