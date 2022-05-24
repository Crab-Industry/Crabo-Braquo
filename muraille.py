import pygame


class Muraille(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.vie = 200
        self.max_vie = 200
        self.image = pygame.image.load("assets/picture/muraille.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 140
        self.jeu = jeu

    def barre_de_vie(self, surface):
        position = [self.rect.x, self.rect.y - 50, self.vie, 8]  # position en x,y la taille et la hauteur
        position2 = [self.rect.x, self.rect.y - 50, self.max_vie, 8]
        pygame.draw.rect(surface, (222, 18, 18), position2)  # barre en arrière plan comme ça on voit la vie max
        pygame.draw.rect(surface, (122, 246, 18), position)  # barre principale

    def degat_subit(self, degats):
        if self.vie - degats > degats:
            self.vie -= degats
        else:
            self.jeu.game_over(True)
