import pygame

#initialisation de pygame
pygame.init()

#titre et icône & creation écran
pygame.display.set_caption("Crabo-Braquo")
icon = pygame.image.load("assets/crabe.png")
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((1000,394))
running = True

# importer un fond d'écran
background = pygame.image.load("assets/desert.png")

# class de notre jeu
class Jeu:
    def __init__(self):
        self.cannon = Cannon()

#Class Canon
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack = 42
        self.image = pygame.image.load("assets/cannon_2.png")
        self.rect = self.image.get_rect()
        self.rect.x=800
        self.rect.y=140

#On importe notre canon
jeu = Jeu()




#Game loop
while running:

    # appliquer l'image sur l'arrière plan du jeu
    screen.blit(background, (0,0))

    # appliquer l'image du cannon
    screen.blit(jeu.cannon.image, jeu.cannon.rect)

    # mettre a jour l'écran
    pygame.display.flip()

    # condition pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

pygame.quit()