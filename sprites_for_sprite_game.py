import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("images/playerShip1_blue.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300
        self.y_speed = 0

    def update(self):
        self.rect.y = self.rect.y + self.y_speed

    def up(self):
        self.y_speed = self.y_speed - 4

    def stop_up(self):
        self.y_speed = self.y_speed + 4


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("images/ufoYellow.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 50
        self.alive = True

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            self.alive = False
