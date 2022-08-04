import pygame

class Dinosaur:
    def __init__(self):
        self.player = pygame.image.load("imgonline-com-ua-Resize-SO1MsSng35k1vaNt.jpg")
        self.player.set_colorkey("WHITE")
        self.playery = 0
        self.jumpUP = False
        self.jumpDown = False

    def jump(self):
        if self.jumpUP == True and self.playery