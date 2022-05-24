import pygame

import math


# Class boulet
class Boulet(pygame.sprite.Sprite):
    def __init__(self, cannon):
        self.cannon = cannon
        super().__init__()
        self.image = pygame.image.load("assets/picture/boulet.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = cannon.rect.x + 10
        self.rect.y = cannon.rect.y + 10
        self.y_save = self.rect.y
        #on convertis l'angle de dégrés à radians, faut faire en sorte que ça fonctionne pour les nb négatifs aussi
        self.angle = (self.cannon.angle_cannon * math.pi )/ 180 #self.cannon.angle_cannon
        self.velocite = 100

    def remove(self):
        self.cannon.all_boulet.remove(self)

    def mouvement(self):
        g = 9.81
        self.rect.x += 10
        self.rect.y = g / (2 * (self.velocite ** 2) * (math.cos(self.angle)) ** 2) * (self.rect.x ** 2) + (math.tan(self.angle) * self.rect.x) + self.y_save


        # supprimer le boulet quand il touche le monstre, infliger des dégats à tous les monstre
        for monstre in self.cannon.jeu.collision(self, self.cannon.jeu.all_monstres):
            self.remove()
            monstre.degat_subit(self.cannon.attaque)
        # détruire les boulet sortie de l'écran
        if self.rect.x > 1000 or self.rect.x < 0 or self.rect.y > 394 or self.rect.y<-50:
            self.remove()
