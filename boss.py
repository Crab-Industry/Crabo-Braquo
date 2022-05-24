"""
Fichier de la classe Boss
Image de la muraille: "assets/picture/King_Crab.png"
"""
import pygame


class Boss(pygame.sprite.Sprite):
    """
    Classe Boss qui gère le boss (Crab King)
    Possède plusieurs fonctions:
        __init__()
        mouv_boss()
        barre_de_vie()
        degat_subit()
        aug_timer()
        barre_de_temps()
    """
    def __init__(self, jeu):
        """
        Fonction: __init__
        --------------------
        self.jeu: Classe Jeu() déjà initialisé
        self.attaque: dégâts d'attaque du Crab King
        self.vie: HP du Crab King
        self.max_vie: HP_max du Crab King
        self.image: Image du crabe, puis transformée en dimension 40*40
        self.rect: masque_rectangle du crabe
        self.rect.x: position x
        self.rect.y: position y
        self.velocite: vitesse du Crab King
        self.timer: temps en tick du jeu
        self.spawn_rate: temps en tick pour apparation du Crab King
        """
        super().__init__()
        self.jeu = jeu
        self.attaque = 10
        self.vie = 3000
        self.max_vie = 3000
        self.image = pygame.image.load("assets/picture/King_Crab.png")
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1001
        self.rect.y = 230
        self.velocite = 1
        self.timer = 0
        self.spawn_rate = 30

    def mouv_boss(self):
        """
        Fonction: mouv_boss()
        --------------------
        Permet le déplacement de monstre et s'arrête si une colision avec la muraille
        """
        # Condition qui permet d'avancer le crabe
        # Détecte la collision avec le crabe
        if not self.jeu.collision(self, self.jeu.all_murailles):
            self.rect.x -= self.velocite
        else:  # le monstre est devant la murailles, il va pouvoir faire des degats
            self.jeu.muraille.degat_subit(self.attaque)

    def barre_de_vie(self, surface):
        """
        Fonction: barre_de_vie
        --------------------
        Permet d'afficher la barre de vie du Crab King
        Dessiné par pygame.draw.rect()

        :var:
            position: barre de self.vie
            position2: barre de self.max_vie

        :param:
            surface: Screen initialisé par pygame
        """
        position = [self.rect.x - 10, self.rect.y - 10, self.vie / 20, 3]  # position en x,y la taille et la hauteur
        position2 = [self.rect.x - 10, self.rect.y - 10, self.max_vie / 20, 3]
        pygame.draw.rect(surface, (115, 115, 115), position2)  # barre en arrière plan comme ça on voit la vie max
        pygame.draw.rect(surface, (122, 246, 18), position)  # barre principale

    def degat_subit(self, degats):
        """
        Fonction: degat_subit
        --------------------
        Fonction qui permet la soustraction de la vie en fonction de dégâts
        Reset le mob s'il meurt

        :param:
            degats: (int) dégâts infligés au Crab King
        """
        self.vie -= degats
        if self.vie <= 0:
            # on supprime le crabe quand il a plus de vie
            self.jeu.all_boss.remove(self)
            self.vie = self.max_vie
            self.rect.x = 1001
            self.jeu.add_score(point=20)

    def aug_timer(self):
        """
        Fonction: aug_timer
        --------------------
        Augmente le timer
        """
        self.timer += 1 / 10

    def barre_de_temps(self, surface):
        """
        Fonction: barre_de_temps
        --------------------
        Permet d'afficher la barre temps de spawn du Crab King
        Dessiné par pygame.draw.rect()

        :var:
            position: barre de self.vie
            position2: barre de self.max_vie

        :param:
            surface: Screen initialisé par pygame
        """
        self.aug_timer()
        position = [10, 20, (400 / self.spawn_rate) * self.timer, 8]  # position en x,y la taille et la hauteur
        position2 = [10, 20, 400, 8]
        pygame.draw.rect(surface, (1, 11, 13), position2)  # barre en arrière plan
        pygame.draw.rect(surface, (222, 18, 18), position)  # barre principale

