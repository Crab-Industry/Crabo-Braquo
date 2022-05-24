"""
Fichier de la classe Muraille
Image de la muraille: "assets/picture/muraille.png"
"""
import pygame


class Muraille(pygame.sprite.Sprite):
    """
    Classe Muraille
    Muraille du jeu
    Possède plusieurs fonctions:
        __init__()
        barre_de_vie()
        degat_subit()
    """
    def __init__(self, jeu):
        """
        Fonction: __init__
        --------------------
        self.vie: HP de la muraille
        self.max_vie: HP_max de la muraille
        self.image: Image de la muraille, puis transformée en dimension 200*200
        self.rect: masque_rectangle de la muraille
        self.rect.x: position x
        self.rect.y: position y
        self.jeu: Import de la classe jeu déjà initialisée
        """
        super().__init__()
        self.vie = 200
        self.max_vie = 200
        self.image = pygame.image.load("assets/picture/muraille.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 140
        self.jeu = jeu

    def barre_de_vie(self, surface):
        """
        Fonction: barre_de_vie
        --------------------
        Permet d'afficher la barre de vie de la muraille
        Dessiné par pygame.draw.rect()

        :var:
            position: barre de self.vie
            position2: barre de self.max_vie

        :param:
            surface: Screen initialisé par pygame
        """
        position = [self.rect.x, self.rect.y - 50, self.vie, 8]  # position en x,y la taille et la hauteur
        position2 = [self.rect.x, self.rect.y - 50, self.max_vie, 8]
        pygame.draw.rect(surface, (222, 18, 18), position2)  # barre en arrière plan comme ça on voit la vie max
        pygame.draw.rect(surface, (122, 246, 18), position)  # barre principale

    def degat_subit(self, degats):
        """
        Fonction: degat_subit
        --------------------
        Fonction qui permet la soustraction de la vie en fonction de dégâts

        :param:
            degats: (int) dégâts infligés à la muraille
        """
        self.vie -= degats