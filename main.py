import pygame
import sys

from dinosaur import Dinosaur
from cactus import Cactus


class Window:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1200, 690))
        pygame.display.set_caption("WTF!")
        self.clock = pygame.time.Clock()
        sky = pygame.Surface((1200, 330))
        sky.fill((255,255,255))

        ground = pygame.Surface((1200,360))
        ground.fill((194,194,194))
        dino = Dinosaur()
        cact = Cactus()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino.jumpUP = True

            if not (dino.playerRect.colliderect(cact.cactusRect)):
                dino.jump()
                cact.move()

            self.window.blit(sky,(0,0))
            self.window.blit(ground, (0,330))
            self.window.blit(cact.body, (cact.cactusRect.x,cact.cactusRect.y))
            self.window.blit(dino.player, (dino.playerRect.x,dino.playerRect.y))
            pygame.display.flip()
            self.clock.tick(60)
Window()