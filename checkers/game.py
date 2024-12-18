# importamos librerias, módulos y constantes que nos puedar ser útiles
import pygame
from .constants import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board

# creamos una clase juego para controlar lo que pasa en una partida
class Game:
    # inicializamos el estatus del juego
    def __init__(self, win):
        self._init()
        self.win = win

    # cuando hay un movimiento actualizamos el tablero
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    # al iniciar una partida el turno siempre será del jugador humano, es decir de las piezas rojas
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    # comprobamos ganador
    def winner(self):
        return self.board.winner()
    
    # cuando iniciamos una patida siempre se inicializa de nuevo el tablero
    def reset(self):
        self._init()

    # método para permitir al jugador de acuerdo a su turno observar los movimientos posibles tras seleccionar una pieza del tablero
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    # cuando el jugador realiza un movimiento, se establece una nueva posición para esa ficha en el tablero y se actualiza el tablero en general
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    # dibujamos un circulo de posible movimiento en tablero
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE,
                               (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

    # alternamos turnos en la partida
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    # traemos el tablero a l interfaz
    def get_board(self):
        return self.board
    
    # después de que el agente hace un movimiento, actualizamos tablero y cambiamos turno
    def ai_move(self, board):
        self.board = board
        self.change_turn()