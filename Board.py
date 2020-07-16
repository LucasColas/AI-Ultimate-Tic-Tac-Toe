import pygame



class new_Board():
    def __init__(self):

    def create_board(self):
        return [[for x in range(3)] for y in range(3)]

    def draw_board(self, Win, Lines_color, Width):
        for i in range(1,3):
            pygame.draw.line(Win, Lines_color, (0, Width*(i/3)), (Width, Width*(i/3)), 1)

    def test(self):
        print("test class new_Board")
