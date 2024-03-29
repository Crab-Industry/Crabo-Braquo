"""
Fichier de la classe Jeu qui gère le jeu
"""
import pygame
import random

from boss import Boss
from canon import Canon
from monstre import Monstre
from muraille import Muraille
from sound import Soundplayer
from timer import Timer


class Jeu:
    """
    Classe jeu qui gère le contrôle du jeu.
    Possède plusieurs fonctions:
        __init__()
        apparition_monstre()
        apparition_boss()
        collision()
        update()
        start_jeu()
        game_over_stats()
        game_over_reset()
        pause_in()
        pause_update()
        pause_out()
        add_score()
    """
    def __init__(self):
        # Statements
        self.lancement = False
        self.pause = False
        self.game_over_statement = False

        # on fait un groupe pour murailles même si ya qu'une
        # muraille car on est obliger pour la fonction collision
        # qui demande un groupe en argument
        self.all_murailles = pygame.sprite.Group()
        self.muraille = Muraille(self)
        self.all_murailles.add(self.muraille)
        # même chose qu'on a fait avec les boulets on crée un
        # groupe pour pouvoir en avoir plusieur
        self.all_monstres = pygame.sprite.Group()
        self.monstre = Monstre(self)
        self.all_boss = pygame.sprite.Group()

        self.boss = Boss(self)
        self.pressed = {
        }
        self.canon = Canon(self)

        # Implémentatino de la classe son
        self.sound_player = Soundplayer()
        # Timer
        self.timer = Timer()

        self.pause_boutton = pygame.image.load("assets/picture/pause_button.png")
        self.pause_boutton = pygame.transform.scale(self.pause_boutton, (36, 36))
        self.pause_boutton_rectangle = self.pause_boutton.get_rect()
        self.pause_boutton_rectangle.x = 930
        self.pause_boutton_rectangle.y = 12

        self.reprendre = pygame.image.load("assets/picture/reprendre.png")
        self.reprendre = pygame.transform.scale(self.reprendre, (331, 101))
        self.reprendre_rectangle = self.reprendre.get_rect()

        self.quitter = pygame.image.load("assets/picture/quitter.png")
        self.quitter = pygame.transform.scale(self.quitter, (331, 101))
        self.quitter_rectangle = self.quitter.get_rect()

        self.king_crab = pygame.image.load("assets/picture/King_Crab.png")
        self.king_crab = pygame.transform.scale(self.king_crab, (48, 48))

        self.game_over_png = pygame.image.load("assets/picture/game over.png")
        self.game_over_png_rectangle = self.game_over_png.get_rect()

        # innitialisation du score à 0
        self.score = 0

    def apparition_monstre(self):
        """
        Fonction: apparition_monstre
        --------------------
        Génère l'apparition de monstre
        """
        self.all_monstres.add(Monstre(self))

    def apparition_boss(self):
        """
        Fonction: apparition_boss
        --------------------
        Génère l'apparition de boss
        """
        self.all_boss.add(Boss(self))

    def collision(self, sprite, group):
        """
        Fonction: collision
        --------------------
        :return:
            détection de collison avec un sprite
        """
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self, screen):
        """
        Fonction: update
        --------------------
        Permet la mise à jour de la fenêtre avec l'action de chaque entité
        """
        # appliquer l'image du canon et de la muraille
        screen.blit(self.canon.image, self.canon.rect)
        screen.blit(self.muraille.image, self.muraille.rect)
        screen.blit(self.pause_boutton, (self.pause_boutton_rectangle.x, self.pause_boutton_rectangle.y))

        self.muraille.barre_de_vie(screen)
        self.boss.barre_de_temps(screen)
        # On recupere les boulets du canon
        for boulet in self.canon.all_boulet:
            boulet.mouvement()
        # même chose on récupere les monstres
        for monstre in self.all_monstres:
            monstre.mouv_monstre()
            monstre.barre_de_vie(screen)
        for boss in self.all_boss:
            boss.mouv_boss()
            boss.barre_de_vie(screen)

        # groupe du boulet pour qu'on le voit
        self.canon.all_boulet.draw(screen)
        # même chose pour les monstre
        self.all_monstres.draw(screen)
        self.all_boss.draw(screen)

        screen.blit(self.king_crab, (425, 8))

        # rotation
        if self.pressed.get(pygame.K_RIGHT):
            self.canon.rotate1()

        elif self.pressed.get(pygame.K_LEFT):
            self.canon.rotate2()

        # Gestion de spawn des mobs en fonction du temps
        if self.timer.counter % 5 == 0:
            for i in range(0, random.randint(0, 2 * (1 + (self.timer.counter // 30)))):
                self.apparition_monstre()
            self.timer.counter += 0.1
            self.monstre.spawnable = False

        if int(self.timer.counter) % 3 == 0 and self.monstre.spawnable is False:
            self.timer.counter = int(self.timer.counter)
            self.monstre.spawnable = True

        if self.boss.timer >= self.boss.spawn_rate:
            self.apparition_boss()
            self.boss.timer = 0

        # affichage du timer
        font = pygame.font.Font("assets/font/TheNextFont.ttf", 25)
        timer_text = font.render(f"Temps : {int(self.timer.counter)}s", 1, (0, 0, 0))
        screen.blit(timer_text, (760, 20))

        # affichage du score
        font = pygame.font.Font("assets/font/TheNextFont.ttf", 25)
        timer_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(timer_text, (500, 20))

    def start_jeu(self):
        """
        Fonction: start_jeu
        --------------------
        Débute le jeu
        """
        self.lancement = True
        self.apparition_monstre()
        # Musique de fond
        self.sound_player.play_sound('background_music')

    def game_over_stats(self, screen):
        """
        Fonction: game_over_stats
        --------------------
        Lance la fenêtre de game_over avec les stats
        """
        if self.game_over_statement is False and self.lancement is True:
            self.game_over_statement = True
            self.sound_player.stop_sound('background_music')
            self.sound_player.play_sound('game_over')
        screen.blit(self.game_over_png, (0, 0))

        font = pygame.font.Font("assets/font/TheNextFont.ttf", 25)
        timer_text = font.render(f"Temps : {int(self.timer.counter)}s", 1, (0, 0, 0))
        screen.blit(timer_text, ((screen.get_width() / 1.75), (screen.get_height() / 1.25)))

        timer_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(timer_text, ((screen.get_width() / 3), (screen.get_height() / 1.25)))

        font = pygame.font.Font("assets/font/TheNextFont.ttf", 25)
        timer_text = font.render(f"Cliquez pour quitter", 1, (0, 0, 0))
        screen.blit(timer_text, ((screen.get_width() / 2.75), (screen.get_height() / 1.1)))

    def game_over_reset(self):
        """
        Fonction: game_over_reset
        --------------------
        Permet le reset des variables des objets et relance le joueur au menu principal
        """
        self.lancement = False
        self.game_over_statement = False
        self.pause = False
        self.sound_player.stop_sound('background_music')
        self.sound_player.stop_sound('game_over')
        self.all_monstres = pygame.sprite.Group()
        self.all_boss = pygame.sprite.Group()
        self.muraille.vie = self.muraille.max_vie
        self.canon = Canon (self)
        self.pressed = {}
        self.timer.reset_time()
        self.score = 0
        self.boss.timer = 0

    def pause_in(self):
        """
        Fonction: pause_in
        --------------------
        Met en pause le jeu
        """
        self.pause = True
        self.sound_player.pause_sound()

    def pause_update(self, screen):
        """
        Fonction: pause_update
        --------------------
        Permet la mise à jour de la fenêtre de pause
        """
        self.reprendre_rectangle.x = (screen.get_width() / 2.85)  # on utiliser pour savoir si on clique dessus
        self.reprendre_rectangle.y = (screen.get_height() / 4)

        self.quitter_rectangle.x = (screen.get_width() / 2.85)  # on utiliser pour savoir si on clique dessus
        self.quitter_rectangle.y = (screen.get_height() / 1.75)

        screen.blit(self.reprendre, (self.reprendre_rectangle.x, self.reprendre_rectangle.y))
        screen.blit(self.quitter, (self.quitter_rectangle.x, self.quitter_rectangle.y))

        font = pygame.font.Font("assets/font/TheNextFont.ttf", 25)
        timer_text = font.render(f"Temps actuel : {int(self.timer.counter)}s", True, (0, 0, 0))
        screen.blit(timer_text, (screen.get_width() / 2, (screen.get_height() / 6.5)))

        font = pygame.font.Font("assets/font/TheNextFont.ttf", 25)
        timer_text = font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(timer_text, (screen.get_width() / 3, (screen.get_height() / 6.5)))

    def pause_out(self):
        """
        Fonction: pause_out
        --------------------
        Reprends le jeu
        """
        self.pause = False
        self.sound_player.unpause_sound()

    def add_score(self, point):
        """
        Fonction: add_score
        --------------------
        Permet l'addition de score en fonction d'entités tuées
        """
        self.score += point
