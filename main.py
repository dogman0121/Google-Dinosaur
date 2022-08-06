import pygame
import sys

from dinosaur import Dinosaur
from cactus import Cactus
from ground import Ground


class Window:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1200, 690))
        pygame.display.set_caption("WTF!")
        self.clock = pygame.time.Clock()
        sky = pygame.Surface((1200, 330))
        sky.fill((255, 255, 255))

        ground = pygame.Surface((1200, 360))
        ground.fill((255, 255, 255))
        dino = Dinosaur()
        cact = Cactus()
        ground1 = Ground()

        timerCouter = 0
        timer = pygame.font.Font("Undertale-Battle-Font.ttf", 18)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino.jumpUP = True



            self.window.blit(sky, (0, 0))
            self.window.blit(ground, (0, 330))

            text = timer.render(str(int(timerCouter)), True, (0, 0, 0))

            self.window.blit(text, (1000, 25))

            if (dino.playerRect.collidelist([i[1] for i in cact.massiv_cactus])) == -1:
                dino.jump()
                cact.move()
                ground1.move()
                timerCouter += 0.15

                if cact.speed != 15:
                    cact.speed = 9 + 1 * (timerCouter // 200)
                    ground1.speed = 9 + 1 * (timerCouter // 200)



            for i in range(3, -1, -1):
                x = ground1.massiv_sprints[i][1].x
                y = ground1.massiv_sprints[i][1].y

                self.window.blit(ground1.massiv_sprints[i][0], (x, y))

            for i in range(len(cact.massiv_cactus)):
                x = cact.massiv_cactus[i][1].x
                y = cact.massiv_cactus[i][1].y

                self.window.blit(cact.massiv_cactus[i][0], (x, y))

            self.window.blit(dino.player, (dino.playerRect.x, dino.playerRect.y))



            pygame.display.flip()
            self.clock.tick(60)
Window()