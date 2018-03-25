import pygame, sys
from random import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speed[1] = - self.speed[1]


def animate(group):
    joohanball.move()
    screen.blit(joohanball.image, joohanball.rect)

    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)

        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = - ball.speed[0]
            ball.speed[1] = - ball.speed[1]
        group.add(ball)

        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    pygame.time.delay(20)


pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
image_file = ('beach_ball.png')

speed = [0, 0]
location = 320, 240
joohanball = Ball(image_file, speed, location)
screen.blit(joohanball.image, joohanball.rect)

group = pygame.sprite.Group()

for y in range(4):
    location = [y * 180 + 10, 100]
    speed = [choice([-2, 2]), choice([-2, 2])]
    ball = Ball(image_file, speed, location)
    screen.blit(ball.image, ball.rect)
    group.add(ball)

pygame.display.flip()

while True:
    screen.fill([255, 255, 255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            joohanball.rect.center = event.pos

    animate(group)

    for ball in group:
        if pygame.sprite.collide_rect(joohanball, ball):
            group.remove(ball)
