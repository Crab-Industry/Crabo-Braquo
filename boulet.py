"""
Fichier de la classe boulet qui contient le boulet
Image du crabe: "assets/picture/boulet.png"
Import de math pour les équations de trajectoires
"""
import pygame
import math


class Boulet(pygame.sprite.Sprite):
    """
    Classe Boulet
    Permet le contrôle de la trajectoire du boulet
    Est généralement appelé par canon.py
    Possède plusieurs fonctions:
        __init__()
        remove()
        mouvement()
    """

    def __init__(self, canon):
        """
        Fonction: __init__
        --------------------
        self.canon: Classe Canon() déjà initialisé
        self.image: Image de la boulet, puis transformée en dimension 40*40
        self.rect: masque_rectangle du boulet
        self.rect.x: position x
        self.rect.y: position y
        self.y_save: duplication de self.rect.y
        self.angle: orientation du cannon (importé depuis canon.py, converti de degré en radian)
        self.velocite: vitesse du boulet
        """
        self.canon = canon
        super().__init__()
        self.image = pygame.image.load("assets/picture/boulet.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = canon.rect.x + 10
        self.rect.y = canon.rect.y + 10
        self.y_save = self.rect.y
        # on convertis l'angle de dégrés à radians, faut faire en sorte que ça fonctionne pour les nb négatifs aussi
        self.angle = (self.canon.angle_canon * math.pi) / 180  # self.canon.angle_canon
        self.velocite = 100

    def remove(self):
        """
        Fonction: remove()
        --------------------
        Suppression du boulet
        """
        self.canon.all_boulet.remove(self)

    def mouvement(self):
        """
        Fonction: mouvement()
        --------------------
        Calcul de trajectoire et appel à self.remove() si collisions avec un monstre
        g = Valeur de la pesanteur à la surface de la Terre
        self.y_save = Hauteur du canon
        self.angle = Angle par rapport à l’horizontale
        """
        g = 9.81
        self.rect.x += 10
        self.rect.y = g / (2 * (self.velocite ** 2) * (math.cos(self.angle)) ** 2) * (self.rect.x ** 2) + (
                    math.tan(self.angle) * self.rect.x) + self.y_save

        # supprimer le boulet quand il touche le monstre, infliger des dégats à tous les monstre
        for monstre in self.canon.jeu.collision(self, self.canon.jeu.all_monstres):
            self.remove()
            monstre.degat_subit(self.canon.attaque)
        for boss in self.canon.jeu.collision(self, self.canon.jeu.all_boss):
            self.remove()
            boss.degat_subit(self.canon.attaque)
        # détruire les boulet sortie de l'écran
        if self.rect.x > 1000 or self.rect.x < 0 or self.rect.y > 320 or self.rect.y < -50:
            self.remove()
