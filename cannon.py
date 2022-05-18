import pygame
from boulet import Boulet
#Class Canon
class Cannon(pygame.sprite.Sprite):
    def __init__(self,jeu):
        super().__init__()
        self.attaque = 50
        self.velocite=10
        self.image = pygame.image.load("assets/cannon2.png")
        self.rect = self.image.get_rect()
        self.rect.x=720
        self.rect.y=120
        self.origin_image=self.image
        self.angle=0
        self.all_boulet=pygame.sprite.Group()
        self.jeu=jeu



    def rotate1(self):
        self.angle-=0.5
        self.image= pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect=self.image.get_rect(center=self.rect.center)
    def rotate2(self):
        self.angle+=0.5
        self.image= pygame.transform.rotozoom(self.origin_image,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def lancer_boulet(self):
        self.all_boulet.add(Boulet(self))






