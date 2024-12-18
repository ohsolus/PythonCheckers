# importams librerías necesarias
import pygame

# Dimensiones del tablero
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 4, 4
SQUARE_SIZE = WIDTH//COLS

# Colores en el tablero, por RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

# Establecemos una imágen de corona para el caso de un peón que llega a ser dama
CROWN = pygame.transform.scale(pygame.image.load('assets/pngimg.com - crown_PNG7.png'), (44, 25))