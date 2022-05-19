'''
import pygame
from cannon import Cannon
pygame.init()
#creation écran
pygame.display.set_caption("Crabo-Braquo") #possibilité de rajouté une icone dans la fenètre en mettant une virgule
screen = pygame.display.set_mode((1000,394))
clock = pygame.time.Clock()
running = True
# importation des images
cannon= pygame.image.load("assets/cannon2.png")
background = pygame.image.load("assets/desert.png")


# position du pivot
pivot = [870, 150]
# resulting rect will be blitted at `rect.topleft + offset`.
image_pos= pygame.math.Vector2(0, 0)
angle = 0

while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        angle += 3
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        angle -= 3
    if keys[pygame.K_f]:
        pivot[0] += 2

    # Rotated version of the image and the shifted rect.
    rotated_image, rect = Cannon.rotate(cannon, angle, pivot, image_pos)

    # Drawing.

    screen.blit(rotated_image, rect)  # Blit the rotated image.
    #pygame.draw.circle(screen, (30, 250, 70), pivot, 3)  # dessine le point pivot
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
'''
