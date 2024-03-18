import pygame

TILEAMOUNT = 60
TILESIZE = 100
while (TILEAMOUNT * TILESIZE) > 1000:
    TILESIZE -= 1
WIDTH = TILEAMOUNT * TILESIZE
HEIGHT = WIDTH
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

