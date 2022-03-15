import pygame

#initialisation de pygame
pygame.init()
#Class Canon
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack = 42
        self.image = pygame.image.load("assets/cannon2.png")
        self.rect = self.image.get_rect()
        self.rect.x=800
        self.rect.y=140
#creation écran
pygame.display.set_caption("Crabo-Braquo") #possibilité de rajouté une icone dans la fenètre en mettant une virgule
screen = pygame.display.set_mode((1000,402))
running = True


# importer un fond d'écran
background = pygame.image.load("assets/desert.png")
icone = pygame.image.load("assets/crabe.png")

#On importe notre canon
cannon = Cannon()

while running:
    #Icone
    pygame.display.set_icon(icone)
    # appliquer l'image sur l'arrière plan du jeu
    screen.blit(background, (0,0))
    # appliquer l'image du cannon
    screen.blit(cannon.image,cannon.rect)
    # mettre a jour l'écran
    pygame.display.flip()

    # condition pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

pygame.quit()