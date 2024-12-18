# importamos constantes y librerias que se necesiten
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame

# Creamos una clase para contrlan los atibutos de una pieza en el tablero
class Piece:
    # tamaño y margen de una ficha 
    PADDING = 15
    OUTLINE = 2

    # método para inicializar posición, color y estatus de una pieza
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    # método para calcular la posición de una pieza
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # método para cambiar el estatus de una pieza de peón a rey
    def make_king(self):
        self.king = True

    # método para dibujar piezas en el tablero 
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    # establecemos la nueva posición de una ficha
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        
    # establecemos color 
    def __repr__(self):
        return str(self.color)