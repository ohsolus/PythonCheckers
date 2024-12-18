#importamos librerias necesarias, clases y constantes 
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax

#establecemos una velocidad de actualización de imágen para dar una sensación de tiempo real, es decir, la imágen se actualizará 60 veces en un segundo
FPS = 60

#levantamos la interfaz, cambiamos el nombre y logo para la ventana
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

#capturamos la posición del ratón
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

#creamos una función main desde donde llamaremos a otros métodos
def main():
    #la ventana estará abierta mientras run = True
    run = True
    #establecemos una variable que controle el tiempo transcurrido en el juego
    clock = pygame.time.Clock()
    #Inicializamos el tablero de juego
    game = Game(WIN)

    while run:
        #Usamos el contador del tiempo para actualizar la imágen de pantalla
        clock.tick(FPS)

        #evaluamos los turnos alternos, en este caso si es turno del agente
        if game.turn == WHITE:
            #Llamamos al algoritmo de minimax pra evaluar el mejor movimiento
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        #si el agente gana la ventana deja de correr run = False
        if game.winner() != None:
            print(game.winner())
            run = False

        # capturamos las acciones del tablero
        # si el usuario clickea la x para salir de la ventana, entonces se cierra la interfaz
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            # En cambio si el usuario está jugando una posición entonces capturamos la posición del mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        # actualizamos el tablero de juego
        game.update()

    # salimos directamente de la ventana si no entramos en el bucle
    pygame.quit()

# Llamamos a la función main
main()