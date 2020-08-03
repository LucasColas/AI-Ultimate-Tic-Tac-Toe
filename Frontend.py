import pygame

def fill(surface, color):
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))


def Draw_pieces(Win,x1,y1,x2,y2, Small_Cross, Small_Circle,Cross, Circle, Small_Square, Square, board, big_board, Small_Square, player):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[y][x] == -1:
                Win.blit(Small_Circle, (x1*Small_Square, y1*Small_Square))

            if board[y][x] == 1:
                Win.blit(Small_Cross, (x1*Small_Square, y1*Small_Square))


    for x in range(len(big_board)):
        for y in range(len(board)):
            if board[y][x] == -1:
                Win.blit(Circle, (x2*Square, y2*Square))

            if board[y][x] == 1:
                Win.blit(Cross, (x1*Square, y1*Square))
