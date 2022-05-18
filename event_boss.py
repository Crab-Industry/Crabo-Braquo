import pygame
class Event:
    def __init__(self):
        self.timer=0

    def aug_timer(self):
        self.timer+=1/10


    def barre_de_temps(self,surface):
        self.aug_timer()
        self.spawn_boss()
        position = [10, 20, (400/100)*self.timer, 8]  # position en x,y la taille et la hauteur
        position2 = [10, 20, 400, 8]
        pygame.draw.rect(surface, (1, 11, 13), position2)  # barre en arrière plan
        pygame.draw.rect(surface, (222, 18, 18), position)  # barre principale
    def spawn_boss(self):
        if self.timer>=100:
            print("le boss apparait")
            self.timer=0

