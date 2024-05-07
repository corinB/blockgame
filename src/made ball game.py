import pygame, sys
from random import *

pygame.init()

# 전역 변수로 pikachu 객체 선언
pikachu = None

# 공 클래스 정의
class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, location, conflictCount=None, image_file=None):
        pygame.sprite.Sprite.__init__(self)
        self.conflictCount = conflictCount
        
        # 이미지 파일이 없는 경우, 충돌 횟수에 따라 이미지를 로드
        if image_file == None:
            self.image = pygame.image.load(self.load_images())
        else:
            self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    # 충돌 횟수에 따라 이미지를 반환하는 함수
    def load_images(self):
        if self.conflictCount == 1:
            return 'blockgame/src/img/gray.png'
        elif self.conflictCount == 2:
            return 'blockgame/src/img/black.png'
        else:
            return 'blockgame/src/img/pikachu.png'

    # 공을 이동시키는 메서드
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = - self.speed[0]
        if self.rect.top < 0:
            self.speed[1] = - self.speed[1]
        if self.rect.bottom > 480:
            self.speed[1] = self.speed[1] * 0

    # 충돌 시 충돌 횟수를 감소시키고 이미지를 변경하는 메서드
    def conflict(self):
        self.conflictCount = self.conflictCount - 1
        self.image = pygame.image.load(self.load_images())

    # 충돌 횟수가 0이 되면 충돌이 해결되었는지 확인하는 메서드
    def isEnd(self):
        if self.conflictCount == 0:
            return True
        else:
            return False

# 공들을 애니메이션화시키는 함수
def animate(group):
    # 흰색 공 이동
    white.move()
    screen.blit(white.image, white.rect)

    # 피카츄 공 이동
    pikachu.move()
    screen.blit(pikachu.image, pikachu.rect)

    # joohan 공 이동
    joohan.move()
    screen.blit(joohan.image, joohan.rect)

    # 그룹의 모든 공 이동
    for ball in group:
        ball.move()

    # 그룹의 모든 공 그리기
    for ball in group:
        screen.blit(ball.image, ball.rect)

    # 화면 업데이트
    pygame.display.flip()
    pygame.time.delay(20)

# 공 그룹 생성 함수
def ballgroup(group):
    c = 0

    # 공들을 격자 형태로 생성
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

# 피카츄 공 생성 함수
def pikachuball():
    global pikachu  # 전역 변수로 선언
    screen.fill([255, 255, 255])
    speed = [0, 0]
    location = 320, 380
    pikachu = Ball(speed, location, 0, 'blockgame/src/img/pikachu.png')
    screen.blit(pikachu.image, pikachu.rect)

    pygame.display.flip()
    return pikachu





# joohan 공 생성 함수
def joohanball():
    speed = [4, 2]
    location = 0, 170
    joohanball = Ball(speed, location, 0, 'blockgame/src/img/ball.png')
    screen.blit(joohanball.image, joohanball.rect)
    return joohanball

# 흰색 공 생성 함수
def whi():
    speed = [0, 0]
    location = 0, 320
    white = Ball(speed, location, 0, 'blockgame/src/img/white.png')
    screen.blit(white.image, white.rect)
    return white

# 마우스로 제어되는 공 생성 함수
def mou():
    speed = [0,0]
    location = 320, 240
    mouse = Ball(speed,location, 0, 'blockgame/src/img/white2.png')
    return mouse

# 재시작 버튼 생성 함수
def re():
    speed = [0,0]
    location = 100, 300
    restart = Ball(speed, location, 0, 'blockgame/src/img/restart.png')
    return restart

# 종료 버튼 생성 함수
def finish():
    speed = [0,0]
    location = 400,300
    end = Ball(speed,location, 0, 'blockgame/src/img/end.png')
    return end

# 게임 종료 메시지 생성 함수
def over():
    speed = [0,0]
    location =250, 100
    gameover = Ball(speed,location,0, 'blockgame/src/img/gameover.png')
    return gameover

# Pygame 초기화 및 화면 생성
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

# 충돌 이미지를 보여주는 시간(밀리초)
collision_image_duration = 500  # 0.5초

# 충돌 이미지가 보여지고 있는지 여부를 나타내는 변수
show_collision_image = False

# 충돌 이미지를 보여주는 시작 시간
collision_image_start_time = 0

# 이미지 바꿔주는 배열
pikachu_images = [pygame.image.load('blockgame/src/img/pikachu.png'),
                  pygame.image.load('blockgame/src/img/pikachu_aya.png')]


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
                # 재시작 코드
                pass

    # 충돌 이미지를 보여줄 때의 처리
    if show_collision_image:
        # 충돌 이미지를 보여주는 시간을 초과하면 다시 원래 이미지로 변경
        if pygame.time.get_ticks() - collision_image_start_time >= collision_image_duration:
            pikachu.image = pikachu_images[0]  # 원래 이미지로 변경
            show_collision_image = False  # 충돌 이미지를 보여주는 상태 해제
        else:
            pikachu.image = pikachu_images[1]  # 충돌 이미지로 설정

    if pika:
        animate(group)

    if joohan.rect.bottom > 480:
        pika = False
        screen.fill([255, 255, 255])
        screen.blit(gameover.image, gameover.rect)
        screen.blit(restart.image, restart.rect)
        screen.blit(end.image, end.rect)
        pygame.display.flip()

    # 충돌 검사
    if pygame.sprite.collide_rect(joohan, pikachu):
        joohan.speed[1] = - joohan.speed[1]
        # 충돌 시 충돌 이미지 설정 및 관련 변수 초기화
        pikachu.image = pikachu_images[1]  # 충돌 이미지로 설정
        show_collision_image = True  # 충돌 이미지를 보여주는 상태로 설정
        collision_image_start_time = pygame.time.get_ticks()  # 충돌 이미지를 보여주는 시작 시간 설정

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
