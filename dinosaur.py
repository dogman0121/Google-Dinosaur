import pygame

class Dinosaur:
    def __init__(self):
        self.player = pygame.Surface((80,80))
        self.playerRect = self.player.get_rect()
        self.player.fill((255,159,24))
        self.playerRect.x = 100
        self.playerRect.y = 251
        self.speed = 20
        self.jumpUP = False

    def jump(self):
        if self.jumpUP:
            self.playerRect.y -= self.speed
            self.speed -= 1
            if self.playerRect.y == 251:
                self.jumpUP = False
                self.speed = 20