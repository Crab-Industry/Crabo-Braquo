import pygame
from cannon import Cannon
from monstre import Monstre
from muraille import Muraille
from event_boss import Event
from boss import Boss


class Jeu:
    def __init__(self):
        # Start du jeu
        self.lancement = False

        # on fait un groupe pour murailles même si ya qu'une
        # muraille car on est obliger pour la fonction collision
        # qui demande un groupe en argument
        self.all_murailles = pygame.sprite.Group()
        self.muraille = Muraille(self)
        self.all_murailles.add(self.muraille)
        # même chose qu'on a fait avec les boulets on crée un
        # groupe pour pouvoir en avoir plusieur
        self.all_monstres = pygame.sprite.Group()
        self.pressed = {
        }
        self.cannon = Cannon(self)
        self.event = Event()
        # self.all_boss=pygame.sprite.Group

    # def apparition_boss(self):
    # boss = Boss(self)
    # self.all_boss.add(boss)

    def appariton_monstre(self):
        monstre = Monstre(self)
        self.all_monstres.add(monstre)

    def collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self, screen):
        # appliquer l'image du cannon et de la muraille
        screen.blit(self.cannon.image, self.cannon.rect)
        screen.blit(self.muraille.image, self.muraille.rect)

        self.muraille.barre_de_vie(screen)
        self.event.barre_de_temps(screen)
        # On recupere les boulets du cannon
        for boulet in self.cannon.all_boulet:
            boulet.mouvement()
        # même chose on récupere les monstres
        for monstre in self.all_monstres:
            monstre.mouv_monstre()
            monstre.barre_de_vie(screen)

        # groupe du boulet pour qu'on le voit
        self.cannon.all_boulet.draw(screen)
        # même chose pour les monstre
        self.all_monstres.draw(screen)

        # rotation
        if self.pressed.get(pygame.K_RIGHT):
            self.cannon.rotate1()

        elif self.pressed.get(pygame.K_LEFT):
            self.cannon.rotate2()

    def start_jeu(self):
        self.lancement = True
        # self.appariton_monstre()
        # self.appariton_monstre()

    def game_over(self):
        # on relance le jeu
        self.all_monstres = pygame.sprite.Group()
        self.muraille.vie = self.muraille.max_vie
        self.lancement = False
