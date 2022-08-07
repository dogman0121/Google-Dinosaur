import pygame
from random import randint

class CactusMove:
    def __init__(self):
        self.massiv_cactus = []
        self.speed = 9

        self.massiv_cactus.append(Cactus())

    def move(self):
        if self.massiv_cactus[-1].rect.x < 1200:

            self.massiv_cactus.append(Cactus())

            for i in range(len(self.massiv_cactus)):
                self.massiv_cactus[i].rect.x -= self.speed

        else:
            for i in range(len(self.massiv_cactus)):
                self.massiv_cactus[i].rect.x -= self.speed

        if self.massiv_cactus[0].rect.x < -50:
            self.massiv_cactus.pop(0)


class Cactus:
    def __init__(self):

        n = randint(1,5)
        self.image = pygame.image.load(f"cactus_model{n}.png")

        self.rect = self.image.get_rect()
        self.rect.x = 1200 + randint(500, 1200)

        if n == 1:
            self.rect.y = 225
        elif n == 2:
            self.rect.y = 273
        elif n == 3:
            self.rect.y = 264
        elif n == 4:
            self.rect.y = 268
        else:
            self.rect.y = 227
