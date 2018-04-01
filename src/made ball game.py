import pygame, sys
from random import *

pygame.init()


class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, location, conflictCount=None, image_file=None):
        pygame.sprite.Sprite.__init__(self)
        self.conflictCount = conflictCount
        if image_file == None:
            self.image = pygame.image.load(self.load_images())
        else:
            self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def load_images(self):
        if self.conflictCount == 1:
            return 'gray.png'
        elif self.conflictCount == 2:
            return 'black.png'
        else:
            return 'pikachu.png'

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = - self.speed[1]
        if self.rect.bottom > 480:
            print('game over')

    #           sys.exit()

    def conflict(self):
        self.conflictCount = self.conflictCount - 1
        self.image = pygame.image.load(self.load_images())

    def isEnd(self):
        if self.conflictCount == 0:
            return True
        else:
            return False


def animate(group):
    pikachu.move()
    screen.blit(pikachu.image, pikachu.rect)

    joohanball.move()
    screen.blit(joohanball.image, joohanball.rect)

    for ball in group:
        ball.move()

    for ball in group:
        screen.blit(ball.image, ball.rect)

    pygame.display.flip()
    pygame.time.delay(20)


def ballgroup(group):
    c = 0

    for x in range(2):
        for y in range(7):
            a = randint(0, 1)
            speed = [0, 0]
            if a == 0:
                conflictCount = randint(1, 2)
                location = [90 * y + 10, 80 * x + 10]

                ball = Ball(speed, location, conflictCount)
                screen.blit(ball.image, ball.rect)

                group.add(ball)
                if conflictCount == 1:
                    c = c + 1
                if conflictCount == 2:
                    c = c + 2
    pygame.time.delay(1000)

    return c


def pikachuball():
    screen.fill([255, 255, 255])
    speed = [0, 0]
    location = 320, 380
    pikachu = Ball(speed, location, 0, 'pikachu.png')
    screen.blit(pikachu.image, pikachu.rect)

    pygame.display.flip()
    return pikachu


def joohanball():
    speed = [10, 5]
    location = 0, 170
    joohanball = Ball(speed, location, 0, 'ball.png')
    screen.blit(joohanball.image, joohanball.rect)
    return joohanball


pygame.init()
screen = pygame.display.set_mode([640, 480])
group = pygame.sprite.Group()
pikachu = pikachuball()
joohanball = joohanball()
c = ballgroup(group)
pygame.key.set_repeat(100, 50)
while True:
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pikachu.rect.centerx = pikachu.rect.centerx + 10
            if event.key == pygame.K_LEFT:
                pikachu.rect.centerx = pikachu.rect.centerx - 10
            if event.key == pygame.K_SPACE:
                pikachu.rect = pikachu.rect.move(pikachu.speed)
                pikachu.speed[1] = pikachu.speed[1] - 5
                if pikachu.rect.top == 360:
                    pikachu.speed[1] = pikachu.speed[1] + 10
                    if pikachu.rect.bottom == 380:
                        pikachu.speed[1] = pikachu.speed[1] - 5

    animate(group)

    if pygame.sprite.collide_rect(joohanball, pikachu):
        joohanball.speed[1] = - joohanball.speed[1]

    for ball in group:
        if pygame.sprite.collide_rect(joohanball, ball):
            ball.conflict()
            c = c - 1

            if ball.isEnd():
                group.remove(ball)

            joohanball.speed[0] = - joohanball.speed[0]
            joohanball.speed[1] = - joohanball.speed[1]
            if c == 0:
                c = ballgroup(group)