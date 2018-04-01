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
            self.speed[1] = self.speed[1] * 0

    def conflict(self):
        self.conflictCount = self.conflictCount - 1
        self.image = pygame.image.load(self.load_images())

    def isEnd(self):
        if self.conflictCount == 0:
            return True
        else:
            return False


def animate(group):
    white.move()
    screen.blit(white.image, white.rect)

    pikachu.move()
    screen.blit(pikachu.image, pikachu.rect)

    joohan.move()
    screen.blit(joohan.image, joohan.rect)

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
    speed = [4, 2]
    location = 0, 170
    joohanball = Ball(speed, location, 0, 'ball.png')
    screen.blit(joohanball.image, joohanball.rect)
    return joohanball


def whi():
    speed = [0, 0]
    location = 0, 320
    white = Ball(speed, location, 0, 'white.png')
    screen.blit(white.image, white.rect)
    return white

def mou():
    speed = [0,0]
    location = 320, 240
    mouse = Ball(speed,location, 0, 'white2.png')
    return mouse

def re():
    speed = [0,0]
    location = 100, 300
    restart = Ball(speed, location, 0, 'restart.png')
    return restart

def finish():
    speed = [0,0]
    location = 400,300
    end = Ball(speed,location, 0, 'end.png')
    return end

def over():
    speed = [0,0]
    location =250, 100
    gameover = Ball(speed,location,0, 'gameover.png')
    return gameover
pygame.init()
screen = pygame.display.set_mode([640, 480])
group = pygame.sprite.Group()
pikachu = pikachuball()
joohan = joohanball()
white = whi()
mouse = mou()
restart = re()
end = finish()
gameover = over()
c = ballgroup(group)
pygame.key.set_repeat(100, 50)
updown = False
pika = True

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
                pikachu.speed[1] = pikachu.speed[1] - 5


        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse.rect.center = event.pos
            screen.blit(mouse.image, mouse.rect)
            if pygame.sprite.collide_rect(mouse, end):
                sys.exit()
            if pygame.sprite.collide_rect(mouse, restart):
                pygame.init()
                screen = pygame.display.set_mode([640, 480])
                group = pygame.sprite.Group()
                pikachu = pikachuball()
                joohan = joohanball()
                white = whi()
                mouse = mou()
                restart = re()
                end = finish()
                gameover = over()
                c = ballgroup(group)
                pygame.key.set_repeat(100, 50)
                updown = False
                pika = True

    if pika:

        animate(group)

    if joohan.rect.bottom > 480:
        pika = False
        screen.fill([255,255,255])
        screen.blit(gameover.image, gameover.rect)
        screen.blit(restart.image, restart.rect)
        screen.blit(end.image, end.rect)

        pygame.display.flip()


    if pygame.sprite.collide_rect(pikachu, white):
        pikachu.speed[1] = pikachu.speed[1] + 10

    if pygame.sprite.collide_rect(joohan, pikachu):
        joohan.speed[1] = - joohan.speed[1]

    for ball in group:
        if pygame.sprite.collide_rect(joohan, ball):
            ball.conflict()
            c = c - 1

            if ball.isEnd():
                group.remove(ball)

            joohan.speed[0] = - joohan.speed[0]
            joohan.speed[1] = - joohan.speed[1]
            if c == 0:
                c = ballgroup(group)