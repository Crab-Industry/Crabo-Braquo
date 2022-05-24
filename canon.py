"""
Fichier de la classe Canon qui contient le canon
Image du crabe: "assets/picture/canon.png"
Import de la classe boulet: "boulet.py"
"""
import pygame

from boulet import Boulet


class Canon(pygame.sprite.Sprite):
    """
    Classe Canon
    Possède plusieurs fonctions:
        __init__()
        rotate1()
        rotate2()
        lancer_boulet()
    """
    def __init__(self, jeu):
        """
        Fonction: __init__
        --------------------
        self.jeu: Classe Jeu() déjà initialisé
        self.attaque: dégâts d'attaque du crabe
        self.image: Image de la muraille, puis transformée en dimension 40*40
        self.rect: masque_rectangle du crabe
        self.rect.x: position x
        self.rect.y: position y
        self.velocite: vitesse du crabe
        self.origin_image: permet de copier le self.image
        self.angle: orientation du cannon
        self.angle_canon: orientation du canon (utilisé dans boulet.py)
        self.all_boulet: classe pygame qui regroupe tous les sprites généré de cette classe
        """
        super().__init__()
        self.jeu = jeu
        self.attaque = 50
        self.image = pygame.image.load("assets/picture/canon.png")
        self.rect = self.image.get_rect()
        self.rect.x = 140
        self.rect.y = 120
        self.velocite = 10
        self.origin_image = self.image
        self.angle = 0
        self.angle_canon = -20
        self.all_boulet = pygame.sprite.Group()

    def rotate1(self):
        """
        Fonction: rotate1
        --------------------
        Modification de la rotation du canon en self.angle - 1 et self.angle_canon - 1
        Transformation de l'orientation de l'image -> pygame.transform.rotozoom()
        """
        self.angle -= 1
        self.angle_canon += 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate2(self):
        """
        Fonction: rotate1
        --------------------
        Modification de la rotation du canon en self.angle + 1 et self.angle_canon + 1
        Transformation de l'orientation de l'image -> pygame.transform.rotozoom()
        """
        self.angle += 1
        self.angle_canon -= 1
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def lancer_boulet(self):
        """
        Fonction: lancer_boulet
        --------------------
        Permet de lancer un boulet
        Ajouté dans le groupe de sprite all_boulet
        """
        self.all_boulet.add(Boulet(self))
