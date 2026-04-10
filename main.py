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

size = (1000, 700)
clock = pygame.time.Clock()
#ventana
screen = pygame.display.set_mode(size)

#coordenadas
cord_x = 100
cord_y = 100

#velocidad de la figura
speedX = 3
speedY = 5


while True:
    for evenet in pygame.event.get():
        print(evenet.type)
        if evenet.type == pygame.QUIT:
            sys.exit()

    #rebote de pantalla
    if(cord_x > 1000 or cord_x < 0 ):
        speedX *= -1
    if (cord_y > 700 or cord_y < 0 ):
        speedY *= -1


    #relleno de pantalla
    screen.fill(WHITE )

    cord_x += speedX
    cord_y += speedY

    for x in range(100,700,100):
        pygame.draw.rect(screen, RED, [cord_x,cord_y,50,40])

    #actualiza la pantallla
    pygame.display.flip()
    clock.tick(200)