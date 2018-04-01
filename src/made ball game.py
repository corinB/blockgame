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

def animate(group, graygroup):
    pikachu.move()
    screen.blit(pikachu.image, pikachu.rect)

    joohanball.move()
    screen.blit(joohanball.image, joohanball.rect)

    for grayball in graygroup:
        grayball.move
    for grayball in graygroup:
        screen.blit(grayball.image, grayball.rect)
    for ball in group:
        ball.move()
    for ball in group:
        screen.blit(ball.image, ball.rect)

    pygame.display.flip()
    pygame.time.delay(20)



pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

speed = [0, 0]
location = 320, 380
pikachu = Ball('pikachu.png', speed, location)
screen.blit(pikachu.image, pikachu.rect)

speed = [10,5]
location = 0,170
joohanball = Ball('ball.png', speed, location)
screen.blit(joohanball.image, joohanball.rect)
group = pygame.sprite.Group()
graygroup = pygame.sprite.Group()
b = 0

for x in range(2):
    for y in range(7):
        a = randint(0, 1)
        
        if a == 0:
            location = [90 * y + 12, 80 * x + 12]
            speed = [0, 0]
            grayball = Ball('gray.png', speed, location)
            screen.blit(grayball.image, grayball.rect)
            graygroup.add(grayball)

            location = [90 * y + 10, 80 * x + 10]
            ball = Ball('black.png', speed, location)
            screen.blit(ball.image, ball.rect)

            group.add(ball)
            
            b = b + 1


pygame.display.flip()

while True:
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif  event.type == pygame.MOUSEMOTION:
            pikachu.rect.centerx = event.pos[0]
              
    animate(group, graygroup)
    
    
    if pygame.sprite.collide_rect(joohanball, pikachu):
        joohanball.speed[1] = - joohanball.speed[1]

    if b > 0:

        for ball in group:
            if pygame.sprite.collide_rect(joohanball, ball):
                group.remove(ball)
                joohanball.speed[0] = - joohanball.speed[0]
                joohanball.speed[1] = - joohanball.speed[1]
                b = b - 1
    
    
    for grayball in graygroup:
        if pygame.sprite.collide_rect(joohanball, grayball):
            graygroup.remove(grayball)
            joohanball.speed[0] = - joohanball.speed[0]
            joohanball.speed[1] = - joohanball.speed[1]