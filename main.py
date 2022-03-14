import pygame

#initialisation de pygame
pygame.init()

#creation écran
pygame.display.set_caption("Crabo-Braquo") #possibilité de rajouté une icone dans la fenètre en mettant une virgule
screen = pygame.display.set_mode((800,600))

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()