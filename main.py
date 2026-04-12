import pygame, sys, time
from pygame import key


pygame.init()

size = (800, 800)
screen = pygame.display.set_mode(size)
tiempo = pygame.time.Clock()

cord_x = 100
cord_y = 200
cord_y2 = 200

#cordenada circulo
circleCordX = 400
circleCordY = 400

#velocidad circulo
velocidadCircle_x = 3
velocidadCircle_y = 2

velocidad_x = 7
velocidad_y = 7
velocidad_y2 = 7

while True:
    for evento in pygame.event.get():
        print(evento.type)
        if evento.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))

    cord_x += velocidad_x

    keys = pygame.key.get_pressed()

    rectangulo = (pygame.draw.rect(screen, (255, 0, 0), (700, cord_y, 50, 100)))
    # Creacion del jugador 1
    if keys[pygame.K_UP]:
        cord_y -= velocidad_y
    elif keys[pygame.K_DOWN]:
        cord_y += velocidad_y
    # limite de recorrido
    if cord_y > 700:
        cord_y = 700
    if cord_y < 0:
        cord_y = 0


    # creacion del jugador 2
    rectangulo2 = (pygame.draw.rect(screen, (0, 255, 0), (50, cord_y2, 50, 100)))

    if keys[pygame.K_w]:
        cord_y2 -= velocidad_y2
    if keys[pygame.K_s]:
        cord_y2 += velocidad_y2
    if cord_y2 > 700:
        cord_y2 = 700
    if cord_y2 < 0:
        cord_y2 = 0

    #bola creacion
    circleCordX += velocidadCircle_x
    circleCordY += velocidadCircle_y
    circulo = (pygame.draw.circle(screen, (255, 0, 0), (circleCordX,circleCordY), 20))

    if circulo.colliderect(rectangulo) or circulo.colliderect(rectangulo2):
        velocidadCircle_x *= -1

    if circleCordY > 800 or circleCordY < 0:
        velocidadCircle_y *= -1



    pygame.display.flip()
    tiempo.tick(60)



