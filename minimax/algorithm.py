# importamos librerias necesarias
from copy import deepcopy
import pygame

# Colores de las fichas
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# definimos la función que aplicará el algoritmo de MiniMax
# el agente evalúa un mínimo y máximo y evalúa todas las jugadas posibles para obtener el mejor resultado (ganar) asumiendo que él es el jugador max y el contrincante humano el jugador min
def minimax(position, depth, max_player, game):
    # evaluamos la posición del jugador
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    # el agente evalúa los movimientos del jugador max, conseguiremos la posición de la pieza y cual sería la mejor jugada posible
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    # evaluamos los movimientos del jugador min para saber cual sería el mejor movimiento
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

# en el tablero vamos a dejar ver todas las evaluaciones de movimientos posibles del agente
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

# evaluamos los movimientos para señalar las posiciones válidas para mover una ficha según posición y color
def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

# señalamos al usuario con color verde sus posibles movimientos en el tablero
def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
