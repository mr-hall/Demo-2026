import pygame
import random

WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOUR = (0,0,0)
FPS = 100
BALLWIDTH = 50

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_speed = 1
        self.y_speed = 0
        self.colour = (255, 0, 0)


    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, BALLWIDTH, BALLWIDTH))

    def update(self):
        self.x = self.x + self.x_speed
        if self.x + BALLWIDTH > WIDTH:
            self.x_speed = - self.x_speed
        if self.x < 0:
            self.x_speed = - self.x_speed

all_sprites = []
for i in range(10):
    ball = Ball(random.randint(0, WIDTH - BALLWIDTH), random.randint(0, HEIGHT - BALLWIDTH))
    all_sprites.append(ball)
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