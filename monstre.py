"""
Fichier de la classe Monstre qui contient le crabe
Image du crabe: "assets/picture/boss_crabe.png"
"""
import pygame
import random


class Monstre(pygame.sprite.Sprite):
    """
    Classe Monstre qui gère les monstres (crabes)
    Possède plusieurs fonctions:
        __init__()
        mouv_monstre()
        barre_de_vie()
        degat_subit()
    """
    def __init__(self, jeu):
        """
        Fonction: __init__
        --------------------
        self.jeu: Classe Jeu() déjà initialisé
        self.attaque: dégâts d'attaque du crabe
        self.vie: HP du crabe
        self.max_vie: HP_max du crabe
        self.image: Image de la muraille, puis transformée en dimension 40*40
        self.rect: masque_rectangle du crabe
        self.rect.x: position x
        self.rect.y: position y
        self.velocite: vitesse du crabe
        self.spawnable: Bool de si le mob est spawnable ou non (gérée par jeu.py)
        """
        super().__init__()
        self.jeu = jeu
        self.attaque = 0.3
        self.vie = 100
        self.max_vie = 100
        self.image = pygame.image.load("assets/picture/boss_crabe.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 1001 - random.randint(0, 200)
        self.rect.y = 300
        self.velocite = random.randint(1, 6)
        self.spawnable = True

    def mouv_monstre(self):
        """
        Fonction: mouv_monstre()
        --------------------
        Permet le déplacement de monstre et s'arrête si une colision avec la muraille
        """
        # Condition qui permet d'avancer le crabe
        # Détecte la colision avec le crabe
        if not self.jeu.collision(self, self.jeu.all_murailles):
            self.rect.x -= self.velocite
        else:  # Le monstre est devant la muraille, il va pouvoir faire des dégâts
            self.jeu.muraille.degat_subit(self.attaque)

    def barre_de_vie(self, surface):
        """
        Fonction: barre_de_vie
        --------------------
        Permet d'afficher la barre de vie du crabe
        Dessiné par pygame.draw.rect()

        :var:
            position: barre de self.vie
            position2: barre de self.max_vie

        :param:
            surface: Screen initialisé par pygame
        """
        position = [self.rect.x - 4, self.rect.y - 10, self.vie / 2, 3]
        position2 = [self.rect.x - 4, self.rect.y - 10, self.max_vie / 2, 3]

        # On dessine d'abord max_vie pour qu'il soit en arrière plan
        pygame.draw.rect(surface, (115, 115, 115), position2)
        pygame.draw.rect(surface, (122, 246, 18), position)

    def degat_subit(self, degats):
        """
        Fonction: degat_subit
        --------------------
        Fonction qui permet la soustraction de la vie en fonction de dégâts
        Reset le mob s'il meurt

        :param:
            degats: (int) dégâts infligés au crabe
        """
        self.vie -= degats
        if self.vie <= 0:
            self.rect.x = 1000 - random.randint(0, 300)
            self.velocite = random.uniform(0.5, 2.0)
            self.vie = self.max_vie
            # on supprime le crabe quand il a plus de vie
            self.jeu.all_monstres.remove(self)
            # on augmente le score
            self.jeu.add_score(point=5)
