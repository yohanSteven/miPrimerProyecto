import sys

import pygame

pygame.init()

#definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

size = (920, 1080)
#ventana
screen = pygame.display.set_mode(size)

while True:
    for evenet in pygame.event.get():
        print(evenet.type)
        if evenet.type == pygame.QUIT:
            sys.exit()
    #relleno de pantalla
    screen.fill(BLACK)

    for x in range(100,700,100):
        pygame.draw.rect(screen, RED, [x,100,100,100])

    #actualiza la pantallla
    pygame.display.flip()
