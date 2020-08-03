import pygame

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def Draw_small_pieces(Win,x,y, Cross, Circle, board, Small_Square, player):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == -1:
                Win.blit(Circle, (x*Small_Square, y*Small_Square))

            if board[y][x] == 1:
                Win.blit(Cross, (x*Small_Square, y*Small_Square))
