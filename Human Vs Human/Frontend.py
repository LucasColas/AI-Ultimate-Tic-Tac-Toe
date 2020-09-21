import pygame

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def Draw_pieces(Win, Small_Cross, Small_Circle,Cross, Circle, Small_Square, Square, board):
    for x1 in range(len(board)):
        for y1 in range(len(board)):
            if board[y1][x1] == -1:

                Win.blit(Small_Circle, (x1*Small_Square, y1*Small_Square))

            if board[y1][x1] == 1:

                Win.blit(Small_Cross, (x1*Small_Square, y1*Small_Square))

def draw_big_pieces(Win, big_board, Square, Circle, Cross):
    for x2 in range(len(big_board)):
        for y2 in range(len(big_board)):
            if big_board[y2][x2] == -1:
                Win.blit(Circle, (x2*Square, y2*Square))

            if big_board[y2][x2] == 1:
                Win.blit(Cross, (x1*Square, y1*Square))



def draw_board(Win, Lines_color, Lines_color_2,Width, Square, Small_Square, margin):
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



def Winner(player):
    if player == -1:
        print("Human wins")

    if player == 1:
        print("AI wins")

    else:
        print("no one wins")
