import pygame
from random import choice

class Ground:
    def __init__(self):
        self.massiv_sprints = []
        for i in range(4):
            image = choice(["ground1.png", "ground2.png", "ground3.png"])

            part  = pygame.image.load(image)
            partRect = part.get_rect()
            partRect.y = 283
            partRect.x = 400 * i
            self.massiv_sprints.append((part, partRect))

    def move(self):
        if self.massiv_sprints[0][1].x < -400:
            self.massiv_sprints.pop(0)
            image = choice(["ground1.png", "ground2.png", "ground3.png"])

            part = pygame.image.load(image)
            partRect = part.get_rect()
            partRect.y = 283
            partRect.x = 1200
            self.massiv_sprints.append((part, partRect))

            for i in range(3, -1, -1):
                self.massiv_sprints[i][1].x -= 10

        else:
            for i in range(3, -1, -1):
                self.massiv_sprints[i][1].x -= 10