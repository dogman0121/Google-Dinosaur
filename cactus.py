import pygame
from random import randint

class Cactus:
    def __init__(self):
        self.massiv_cactus = []

        body = pygame.Surface((50,120))
        cactusRect = body.get_rect()
        body.fill((9,134,86))
        cactusRect.x = 1200 + randint(500,1200)
        cactusRect.y = 210
        self.massiv_cactus.append((body, cactusRect))

    def move(self):
        if self.massiv_cactus[-1][1].x < 1200:
            body = pygame.Surface((50, 120))
            cactusRect = body.get_rect()
            body.fill((9, 134, 86))
            cactusRect.x = 1200 + randint(500, 1200)
            cactusRect.y = 210
            self.massiv_cactus.append((body, cactusRect))

            for i in range(len(self.massiv_cactus)):
                self.massiv_cactus[i][1].x -= 10

        else:
            for i in range(len(self.massiv_cactus)):
                self.massiv_cactus[i][1].x -= 10

        if self.massiv_cactus[0][1].x < -50:
            self.massiv_cactus.pop(0)