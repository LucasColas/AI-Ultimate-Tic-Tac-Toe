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

        #Small Boards
        for move in range(0,3):
            for ab in range(0,3):
                for x in range(1,3): #Vertical lines
                    pygame.draw.line(Win, Lines_color_2, (margin + Square*move, (x*Small_Square) + ab*Square), ((Square-margin) + Square*move,(x*Small_Square) + ab*Square), 1)

                for bc in range(0,2):
                    for y in range(3): #Horizontal lines
                        pygame.draw.line(Win, Lines_color_2, (Small_Square + bc*Small_Square + move*Square, margin + ab*Square), (Small_Square + bc*Small_Square + move*Square, (Square-margin) + ab*Square), 1)

        #Big Board
        for i in range(1,3): #Draw horizontal lines
            pygame.draw.line(Win, Lines_color, (0, Square*i), (Width, Square*i), 2)

        for j in range(1,3): #Draw vertical lines
            pygame.draw.line(Win, Lines_color, (Square*j, 0), (Square*j, Height), 2)



    def test(self):
        print(self.hi)
