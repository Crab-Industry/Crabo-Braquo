import pygame

#Class Canon
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack = 42
        self.image = pygame.image.load("assets/cannon_2.png")
        self.rect = self.image.get_rect()
        self.rect.x=800
        self.rect.y=140