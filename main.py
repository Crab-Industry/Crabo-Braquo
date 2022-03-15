import pygame

#initialisation de pygame
pygame.init()

#creation écran
pygame.display.set_caption("Crabo-Braquo") #possibilité de rajouté une icone dans la fenètre en mettant une virgule
screen = pygame.display.set_mode((1000,394))
running = True


# importer un fond d'écran
background = pygame.image.load("assets/desert.png")


while running:

    # appliquer l'image sur l'arrière plan du jeu
    screen.blit(background, (0,0))

    # mettre a jour l'écran
    pygame.display.flip()

    # condition pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

pygame.quit()