import pygame
import sys

from dinosaur import Dinosaur
from cactus import CactusMove
from ground import Ground


class Window:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1200, 690))
        pygame.display.set_caption("WTF!")
        self.clock = pygame.time.Clock()

        # инициализируем классы
        dino = Dinosaur()
        cact = CactusMove()
        ground = Ground()

        start_play = False

        # добавляем классы
        timerCouter = 0
        timer = pygame.font.Font("Undertale-Battle-Font.ttf", 18)

        record = 0

        endGame = pygame.font.Font("Undertale-Battle-Font.ttf", 50)
        endGameSprite = endGame.render("G A M E  O V E R", True, (110, 109, 110))
        imageEnd = pygame.image.load("restart.png")

        while True:
            collide = pygame.sprite.spritecollide(dino, cact.massiv_cactus, False)

            # обработчик событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        dino.jumpUP = True
                        if not start_play:
                            start_play = True
                        else:
                            if collide != []:
                                record = int(timerCouter)
                                cact = CactusMove()
                                ground = Ground()
                                timerCouter = 0

            self.window.fill((255, 255, 255))

            text = timer.render(str(int(timerCouter)), True, (110, 109, 110))
            counterRect = text.get_rect()
            counterRect.bottomright = (1050, 40)

            recordSprite = timer.render(str(record), True, (110, 109, 110))
            recordRect = recordSprite.get_rect()
            recordRect.bottomright = (950, 40)

            self.window.blit(text, (counterRect.x, counterRect.y))
            self.window.blit(recordSprite, (recordRect.x, recordRect.y))

            collide = pygame.sprite.spritecollide(dino, cact.massiv_cactus, False, pygame.sprite.collide_mask )

            # проверка на сталкивания
            if collide == [] and start_play:
                dino.jump()
                cact.move()
                ground.move()
                timerCouter += 0.15


            if cact.speed != 17:
                cact.speed = 9 + 2 * (timerCouter // 200)
                ground.speed = 9 + 2 * (timerCouter // 200)

            # отрисовка земли
            for i in range(3, -1, -1):
                x = ground.massiv_sprints[i][1].x
                y = ground.massiv_sprints[i][1].y

                self.window.blit(ground.massiv_sprints[i][0], (x, y))

            # отрисовка кактусов
            for i in range(len(cact.massiv_cactus)):
                x = cact.massiv_cactus[i].rect.x
                y = cact.massiv_cactus[i].rect.y

                self.window.blit(cact.massiv_cactus[i].image, (x, y))

            # отрисовка динозаврика
            self.window.blit(dino.image, (dino.rect.x, dino.rect.y))

            if collide != []:
                dino.image = dino.playerDead
                self.window.blit(endGameSprite, (375, 100))
                self.window.blit(imageEnd, (520, 150))

            elif not (dino.jumpUP):
                if int(timerCouter) % 2 == 1:
                    dino.image = dino.playerAct1
                elif int(timerCouter) % 2 == 0 and int(timerCouter) > 0:
                    dino.image = dino.playerAct2
                else:
                    dino.image = dino.playerAtStart
            else:
                dino.image = dino.playerAtStart

            pygame.display.flip()
            self.clock.tick(60)
Window()