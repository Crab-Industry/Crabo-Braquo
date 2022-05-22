import pygame
import random


class Monstre(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.attaque = 0.3
        self.vie = 100
        self.max_vie = 100
        self.image = pygame.image.load("assets/picture/boss_crabe.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 1001 - random.randint(0, 200)
        self.rect.y = 300
        self.velocite = random.randint(1, 3)

    def mouv_monstre(self):
        # verification pour que le monstre ne puisse avancer
        # quand il entre en collision avec la muraille
        if not self.jeu.collision(self, self.jeu.all_murailles):
            self.rect.x -= self.velocite
        else:  # le monstre est devant la murailles, il va pouvoir faire des degats
            self.jeu.muraille.degat_subit(self.attaque)

    def barre_de_vie(self, surface):
        position = [self.rect.x - 4, self.rect.y - 10, self.vie / 2, 3]  # position en x,y la taille et la hauteur
        position2 = [self.rect.x - 4, self.rect.y - 10, self.max_vie / 2, 3]
        pygame.draw.rect(surface, (115, 115, 115), position2)  # barre en arrière plan comme ça on voit la vie max
        pygame.draw.rect(surface, (122, 246, 18), position)  # barre principale

    def degat_subit(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            self.rect.x = 1 - random.randint(0, 300)
            self.velocite = random.uniform(0.5, 2.0)
            self.vie = self.max_vie
            # on supprime le crabe quand il a plus de vie
            # self.jeu.all_monstres.remove(self)
