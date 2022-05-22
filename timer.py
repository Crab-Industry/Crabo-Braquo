import pygame


class Timer:
    def __init__(self):
        # Timer
        self.counter = 1
        self.mytimerevent = pygame.USEREVENT + 1
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(self.mytimerevent, 1000)

    def update_time(self, screen):
        # Timer
        self.counter += 1
        self.clock.tick(60)

    def reset_time(self):
        self.counter = 0
