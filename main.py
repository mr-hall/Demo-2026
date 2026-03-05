import pygame
import random

WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOUR = (0,0,0)
FPS = 100
BALLWIDTH = 50
PADDLELENGTH = 200
PADDLEMARGIN = 20

class Sprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = (255, 0, 0)
        self.width = BALLWIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width , self.height))

    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed


class Ball(Sprite):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.height = BALLWIDTH
        self.x_speed = random.randint(1,3)
        self.y_speed = random.randint(-2,2)


    def update(self):
        self.x = self.x + self.x_speed
        if self.x + BALLWIDTH > WIDTH:
            self.x_speed = - self.x_speed
        if self.x < 0:
            self.x_speed = - self.x_speed

        self.y = self.y + self.y_speed
        if self.y + BALLWIDTH > HEIGHT:
            self.y_speed = - self.y_speed
        if self.y < 0:
            self.y_speed = - self.y_speed

class Paddle(Sprite):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.x_speed = 0
        self.y_speed = 0
        self.height = PADDLELENGTH



all_sprites = []
for i in range(1):
    ball = Ball(random.randint(0, WIDTH - BALLWIDTH), random.randint(0, HEIGHT - BALLWIDTH))
    all_sprites.append(ball)

y = (HEIGHT / 2) - (PADDLELENGTH/2)
left_paddle = Paddle(PADDLEMARGIN, y)
right_paddle = Paddle(WIDTH - BALLWIDTH - PADDLEMARGIN ,y)
all_sprites.append(left_paddle)
all_sprites.append(right_paddle)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    screen.fill(BACKGROUND_COLOUR)
    for sprite in all_sprites:
        sprite.draw(screen)

    for sprite in all_sprites:
        sprite.update()
    pygame.display.flip()
    clock.tick(FPS)