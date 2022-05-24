import pygame
import random
from timer import Timer
class Boss(pygame.sprite.Sprite):
    def __init__(self,jeu):
        super().__init__()
        self.jeu=jeu
        self.attaque = 10
        self.vie = 400
        self.max_vie = 400
        self.image = pygame.image.load("assets/picture/King_Crab.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1001 - random.randint(0, 200)
        self.rect.y = 230
        self.velocite = 1
        self.timer = Timer()


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


    def barre_de_temps(self, surface):

        self.spawn_boss()
        position = [10, 20, (400 / 100) * self.timer.counter, 8]  # position en x,y la taille et la hauteur
        position2 = [10, 20, 400, 8]
        pygame.draw.rect(surface, (1, 11, 13), position2)  # barre en arrière plan
        pygame.draw.rect(surface, (222, 18, 18), position)  # barre principale

    def spawn_boss(self):
        if self.timer.counter %5==0:
            print("le boss apparait")
            self.jeu.all_boss.add(self)
