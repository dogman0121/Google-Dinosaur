import pygame


class Cactus:
    def __init__(self):
        self.body = pygame.Surface((50,120))
        self.cactusRect = self.body.get_rect()
        self.body.fill((9,134,86))
        self.cactusRect.x = 1200
        self.cactusRect.y = 210

    def move(self):
        self.cactusRect.x -= 10
        if self.cactusRect.x < -50:
            self.cactusRect.x = 1200