import pygame
import sys

from dinosaur import Dinosaur


class Window:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1200, 690))
        pygame.display.set_caption("WTF!")

        sky = pygame.Surface((1200, 330))
        sky.fill((255,255,255))

        ground = pygame.Surface((1200,360))
        ground.fill((194,194,194))
        dino = Dinosaur()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino.jumpUP = True

            dino.jump()

            self.window.blit(sky,(0,0))
            self.window.blit(ground, (0,330))
            self.window.blit(dino.player, (100,255))
            pygame.display.flip()
Window()