import pygame
import math


# Class boulet

class Boulet(pygame.sprite.Sprite):
    def __init__(self, cannon):
        self.cannon = cannon
        super().__init__()
        self.image = pygame.image.load("assets/boulet.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = cannon.rect.x

        self.velocite = 94.7

    def remove(self):
        self.cannon.all_boulet.remove(self)

    def mouvement(self):
        g = 9.81
        self.rect.x -= 3
        self.rect.y = ((g) / (2 * (self.velocite ** 2) * (math.cos(2.61) ** 2))) * ((self.rect.x) ** 2) + (
                    math.tan(2.61) * (self.rect.x)) + 120
        print(self.rect.y)
        print(self.rect.x)

        # supprimer le boulet quand il touche le monstre,infliger des dégats à tous les monstre
        for monstre in self.cannon.jeu.collision(self, self.cannon.jeu.all_monstres):
            self.remove()
            print("le boulet a bien toucher le monstre")
            monstre.degat_subit(self.cannon.attaque)
        # détruire les boulet sortie de l'écran
        if self.rect.x > 1000 or self.rect.x < 0:
            self.remove()
            print("boulet supprimer")
