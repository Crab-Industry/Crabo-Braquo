"""
Fichier principal du projet
Fichier à lancer pour lancer le jeu
Auteurs : Crabe Industry© 2022 | Groupe F-4
"""
import pygame

from jeu import Jeu

# Initialisation du module pygame
pygame.init()

pygame.display.set_caption("Crabo-Braquo")
screen = pygame.display.set_mode((1000, 394))

# Importation de ressources (fond-d'écran et logo app)
image_fond = pygame.image.load("assets/picture/desert.jpg")
icone = pygame.image.load("assets/picture/crabe.png")

# Chargement de la classe jeu
jeu = Jeu()

running = True
tuto_menu = False

while running:
    # Icône
    pygame.display.set_icon(icone)

    # Image d'arrière-plan du jeu
    screen.blit(image_fond, (0, 0))

    # Génération des ressources
    image_start = pygame.image.load("assets/picture/CraboBraquo.png")
    image_start = pygame.transform.scale(image_start, (533, 165))
    logo_rectangle_x = (screen.get_width() / 4)
    logo_rectangle_y = (screen.get_height() / 9)

    start = pygame.image.load("assets/picture/start2.png")
    start = pygame.transform.scale(start, (265, 81))
    start_rectangle = start.get_rect()
    start_rectangle.x = (screen.get_width() / 9)
    start_rectangle.y = (screen.get_height() / 1.75)

    tuto = pygame.image.load("assets/picture/tuto.png")
    tuto = pygame.transform.scale(tuto, (265, 81))
    tuto_rectangle = tuto.get_rect()
    tuto_rectangle.x = (screen.get_width() / 2.55)
    tuto_rectangle.y = (screen.get_height() / 1.75)

    quitter = pygame.image.load("assets/picture/quitter.png")
    quitter = pygame.transform.scale(quitter, (265, 81))
    quitter_rectangle = quitter.get_rect()
    quitter_rectangle.x = (screen.get_width() / 1.5)
    quitter_rectangle.y = (screen.get_height() / 1.75)

    tuto_png = pygame.image.load("assets/picture/tuto_png.png")
    tuto_png = pygame.transform.scale(tuto_png, (1000, 394))
    tuto_png_rectangle = tuto_png.get_rect()
    tuto_png_rectangle.x = 0
    tuto_png_rectangle.y = 0

    if jeu.muraille.vie <= 0:
        # Fenêtre de game_over stats
        jeu.game_over_stats(screen)
        if jeu.game_over_statement is True:
            jeu.game_over_stats(screen)
            jeu.lancement = False
        elif jeu.game_over_statement is False:
            jeu.game_over_reset()
    elif jeu.lancement:
        if jeu.pause:
            # Fenêtre de pause
            jeu.pause_update(screen)
        else:
            # Fenêtre du jeu
            jeu.update(screen)
    elif tuto_menu:
        # Fenêtre du tuto
        screen.blit(tuto_png, (tuto_png_rectangle.x, tuto_png_rectangle.y))
    else:
        # Menu principal
        screen.blit(image_start, (logo_rectangle_x, logo_rectangle_y))
        screen.blit(start, (start_rectangle.x, start_rectangle.y))
        screen.blit(tuto, (tuto_rectangle.x, tuto_rectangle.y))
        screen.blit(quitter, (quitter_rectangle.x,  quitter_rectangle.y))

    # Permet la mise à jour de la fenêtre
    pygame.display.flip()

    # Détection de fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        # Détection de l'action du clavier
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            # Permet l'interaction avec la barre espace
            if event.key == pygame.K_SPACE:
                if jeu.lancement is True and jeu.pause is False:
                    jeu.canon.lancer_boulet()
                    jeu.sound_player.play_sound("canon")
                elif jeu.game_over_statement is True:
                    jeu.game_over_statement = False
            elif event.key == pygame.K_ESCAPE:
                if jeu.lancement is True and jeu.pause is False and jeu.game_over_statement is False:
                    jeu.pause_in()
                elif jeu.lancement is True and jeu.pause is True:
                    jeu.pause_out()
                elif jeu.lancement is False and jeu.pause is False and jeu.game_over_statement is True:
                    jeu.game_over_statement = False
                    jeu.lancement = False
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False

        # Permet l'interaction entre la souris et les buttons
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rectangle.collidepoint(event.pos) and jeu.lancement is False and jeu.game_over_statement is False:
                jeu.start_jeu()
                jeu.sound_player.play_sound("click")
            elif tuto_rectangle.collidepoint(event.pos) and jeu.lancement is False and tuto_menu is False and jeu.game_over_statement is False:
                tuto_menu = True
            elif tuto_png_rectangle.collidepoint(event.pos) and jeu.lancement is False and tuto_menu is True:
                tuto_menu = False
            elif jeu.pause_boutton_rectangle.collidepoint(event.pos) and jeu.lancement is True and jeu.pause is False and jeu.game_over_statement is False:
                jeu.pause_in()
            elif jeu.reprendre_rectangle.collidepoint(event.pos) and jeu.lancement is True and jeu.pause is True:
                jeu.pause_out()
            elif jeu.quitter_rectangle.collidepoint(event.pos) and jeu.lancement is True and jeu.pause is True:
                jeu.pause_out()
                jeu.game_over_reset()
            elif jeu.game_over_png_rectangle.collidepoint(event.pos) and jeu.game_over_statement is True:
                jeu.game_over_statement = False
                jeu.lancement = False
            elif quitter_rectangle.collidepoint(event.pos) and jeu.lancement is False and tuto_menu is False and jeu.game_over_statement is False:
                pygame.quit()
                quit()

        if event.type == pygame.USEREVENT + 1 and jeu.pause is False:
            if jeu.lancement:
                jeu.timer.update_time()