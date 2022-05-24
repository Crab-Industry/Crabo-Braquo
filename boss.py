import pygame
import random

class Boss(pygame.sprite.Sprite):
    def __init__(self,jeu):
        super().__init__()
        self.jeu=jeu
        self.attaque = 10
        self.vie = 200
        self.max_vie = 200
        self.image = pygame.image.load("assets/picture/King_Crab.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 1001 - random.randint(0, 200)
        self.rect.y = 300
        self.velocite = 1


    def mouv_boss(self):
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
            # on supprime le crabe quand il a plus de vie
            self.jeu.all_boss.remove(self)