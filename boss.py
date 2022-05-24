import pygame
import random


class Boss(pygame.sprite.Sprite):
    def __init__(self, jeu):
        super().__init__()
        self.jeu = jeu
        self.attaque = 10
        self.vie = 3000
        self.max_vie = 3000
        self.image = pygame.image.load("assets/picture/King_Crab.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1001
        self.rect.y = 230
        self.velocite = 1
        self.timer = 0
        self.spawn_rate = 30

    def mouv_boss(self):
        # verification pour que le monstre ne puisse avancer
        # quand il entre en collision avec la muraille
        if not self.jeu.collision(self, self.jeu.all_murailles):
            self.rect.x -= self.velocite
        else:  # le monstre est devant la murailles, il va pouvoir faire des degats
            self.jeu.muraille.degat_subit(self.attaque)

    def barre_de_vie(self, surface):
        position = [self.rect.x - 4, self.rect.y - 10, self.vie / 4, 3]  # position en x,y la taille et la hauteur
        position2 = [self.rect.x - 4, self.rect.y - 10, self.max_vie / 4, 3]
        pygame.draw.rect(surface, (115, 115, 115), position2)  # barre en arrière plan comme ça on voit la vie max
        pygame.draw.rect(surface, (122, 246, 18), position)  # barre principale

    def degat_subit(self, degats):
        self.vie -= degats
        if self.vie <= 0:
            # on supprime le crabe quand il a plus de vie
            self.jeu.all_boss.remove(self)
            self.vie = self.max_vie
            self.rect.x = 1001
            self.jeu.add_score(point=20)

    def aug_timer(self):
        self.timer += 1 / 10

    def barre_de_temps(self, surface):
        self.aug_timer()
        position = [10, 20, (400 / self.spawn_rate) * self.timer, 8]  # position en x,y la taille et la hauteur
        position2 = [10, 20, 400, 8]
        pygame.draw.rect(surface, (1, 11, 13), position2)  # barre en arrière plan
        pygame.draw.rect(surface, (222, 18, 18), position)  # barre principale

