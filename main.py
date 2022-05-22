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
while running:
    # Icone
    pygame.display.set_icon(icone)

    # appliquer l'image sur l'arrière plan du jeu
    screen.blit(image_fond, (0, 0))

    # appliquer l'image de lancement du jeu le bouton start aussi
    image_start = pygame.image.load("assets/picture/CraboBraquo.png")
    image_start = pygame.transform.scale(image_start, (800, 225))

    start = pygame.image.load("assets/picture/start.png")
    start = pygame.transform.scale(start, (200, 200))
    start_rectangle = start.get_rect()  # on recupère le rectangle
    # on utiliser pour savoir si on clique dessus
    start_rectangle.x = (screen.get_width() / 2.4)
    start_rectangle.y = 180

    if jeu.lancement:
        jeu.update(screen)
    else:
        screen.blit(image_start, (screen.get_width() / 8, 30))
        screen.blit(start, (start_rectangle.x, start_rectangle.y))

    # mettre a jour l'écran
    pygame.display.flip()
    # condition pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # detection touche clavier
        elif event.type == pygame.KEYDOWN:
            jeu.pressed[event.key] = True
            # si la barre espace est appuyer on lance un boulet
            if event.key == pygame.K_SPACE:
                if jeu.lancement is True:
                    jeu.cannon.lancer_boulet()
                    jeu.sound_player.play_sound("canon")
        elif event.type == pygame.KEYUP:
            jeu.pressed[event.key] = False
        # clique de souris
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rectangle.collidepoint(event.pos) and jeu.lancement is False:
                jeu.start_jeu()
                jeu.sound_player.play_sound("click")
