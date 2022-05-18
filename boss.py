import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attaque = 10
        self.vie = 200
        self.max_vie = 200
        self.image = pygame.image.load("assets/King_Crab.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect=self.image.get_rect()