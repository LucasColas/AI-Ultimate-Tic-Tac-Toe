import pygame

Lines_color = (211,211,211)

class new_Board():
    def __init__(self, Win):
        self.Win = Win

    def create_board(self):
        return [[for x in range(3)] for y in range(3)]

    def draw_board(self):
        for i in range(1,3):
            pygame.draw.line(Win, Lines_color,)

    def test(self):
        print("test class new_Board")
