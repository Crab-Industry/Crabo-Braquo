import pygame

#initialisation
pygame.init()
#création de la fennêtre
screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load('images/background.jpg')

#titre et icône
pygame.display.set_caption("Crabo Braquo")
icon = pygame.image.load('images/crabe.png')
pygame.display.set_icon(icon)

#joueur

playerImg = pygame.image.load('images/canon.png')
playerX = 10
playerY = 500

def player():
    screen.blit(playerImg, (playerX, playerY))


#Game loop
open = True
while open:

    screen.fill((255,255,255))
    #background
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False

    player()
    pygame.display.update()
