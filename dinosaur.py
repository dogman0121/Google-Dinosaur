import pygame

class Dinosaur:
    def __init__(self):
        self.image = pygame.image.load("dinosaur_on_start.png")
        self.playerAtStart = pygame.image.load("dinosaur_on_start.png")
        self.playerAct1 = pygame.image.load("dinosaur_animation_run1.png")
        self.playerAct2 = pygame.image.load("dinosaur_animation_run2.png")
        self.playerDead = pygame.image.load("dinosaur_dead.png")
        self.rect = self.image.get_rect()
        # self.player.fill((255,159,24))
        self.rect.x = 100
        self.rect.y = 251
        self.speed = 20
        self.jumpUP = False

    def jump(self):
        if self.jumpUP:
            self.rect.y -= self.speed
            self.speed -= 1
            if self.rect.y == 251:
                self.jumpUP = False
                self.speed = 20