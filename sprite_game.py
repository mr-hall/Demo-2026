import pygame
import sprites_for_sprite_game
WIDTH = 500
HEIGHT = 500
BACKGROUND_COLOUR = (0,0,0)
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
player = sprites_for_sprite_game.Player()
enemy = sprites_for_sprite_game.Enemy()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.up()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.stop_up()
    player.update()
    enemy.check_collision(player)
    screen.fill(BACKGROUND_COLOUR)
    screen.blit(player.image, player.rect)
    if enemy.alive:
        screen.blit(enemy.image, enemy.rect)
    pygame.display.flip()
    clock.tick(FPS)