import pygame

WIDTH, HEIGHT = 400, 400
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/pngimg.com - crown_PNG7.png'), (44, 25))