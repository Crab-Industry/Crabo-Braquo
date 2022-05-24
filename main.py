import time
import pygame

from jeu import Jeu

# initialisation de pygame
pygame.init()
# class de notre jeu

# creation écran
pygame.display.set_caption("Crabo-Braquo")  # possibilité de rajouté une icone dans la fenètre en mettant une virgule
screen = pygame.display.set_mode((1000, 394))

# importer un fond d'écran
image_fond = pygame.image.load("assets/picture/desert.jpg")
icone = pygame.image.load("assets/picture/crabe.png")

# On charge la class jeu
jeu = Jeu()

running = True
tuto_menu = False

while running:
    # Icone
    pygame.display.set_icon(icone)

    # appliquer l'image sur l'arrière plan du jeu
    screen.blit(image_fond, (0, 0))

    # appliquer l'image de lancement du jeu le bouton start aussi
    image_start = pygame.image.load("assets/picture/CraboBraquo.png")
    image_start = pygame.transform.scale(image_start, (533, 165))
    logo_rectangle_x = (screen.get_width() / 4)
    logo_rectangle_y = (screen.get_height() / 9)

    start = pygame.image.load("assets/picture/start2.png")
    start = pygame.transform.scale(start, (265, 81))
    start_rectangle = start.get_rect()  # on recupère le rectangle
    start_rectangle.x = (screen.get_width() / 9)    # on utiliser pour savoir si on clique dessus
    start_rectangle.y = (screen.get_height() / 1.75)

    tuto = pygame.image.load("assets/picture/tuto.png")
    tuto = pygame.transform.scale(tuto, (265, 81))
    tuto_rectangle = tuto.get_rect()
    tuto_rectangle.x = (screen.get_width() / 2.55)    # on utiliser pour savoir si on clique dessus
    tuto_rectangle.y = (screen.get_height() / 1.75)

    quitter = pygame.image.load("assets/picture/quitter.png")
    quitter = pygame.transform.scale(quitter, (265, 81))
    quitter_rectangle = quitter.get_rect()
    quitter_rectangle.x = (screen.get_width() / 1.5)    # on utiliser pour savoir si on clique dessus
    quitter_rectangle.y = (screen.get_height() / 1.75)

    tuto_png = pygame.image.load("assets/picture/tuto_png.png")
    tuto_png = pygame.transform.scale(tuto_png, (1000, 394))
    tuto_png_rectangle = tuto_png.get_rect()
    tuto_png_rectangle.x = 0
    tuto_png_rectangle.y = 0

    if jeu.muraille.vie <= 0:
        jeu.game_over_stats(screen)
        if jeu.game_over_statement is True:
            jeu.game_over_stats(screen)
            jeu.lancement = False
        elif jeu.game_over_statement is False:
            jeu.game_over_reset()
    elif jeu.lancement:
        if jeu.pause:
            # Fenêtre de pause à implémenter
            jeu.pause_update(screen)
        else:
            jeu.update(screen)
    elif tuto_menu:
        screen.blit(tuto_png, (tuto_png_rectangle.x, tuto_png_rectangle.y))
    else:
        screen.blit(image_start, (logo_rectangle_x, logo_rectangle_y))
        screen.blit(start, (start_rectangle.x, start_rectangle.y))
        screen.blit(tuto, (tuto_rectangle.x, tuto_rectangle.y))
        screen.blit(quitter, (quitter_rectangle.x,  quitter_rectangle.y))

    # mettre a jour l'écran
    pygame.display.flip()

    # condition pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        # detection touche clavier
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            # si la barre espace est appuyer on lance un boulet
            if event.key == pygame.K_SPACE:
                if jeu.lancement is True and jeu.pause is False:
                    jeu.cannon.lancer_boulet()
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

        # clique de souris
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