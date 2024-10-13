import pygame
from scripts.player import Player
from scripts.functions import load_image
from scripts.bullet import Bullet

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)

clock = pygame.time.Clock()

FPS = 60

bullets = list()

background = load_image('image\\background.png', (800, 600), None)

bullet_image = load_image('image\\bullet.png', (35, 40), (0, 0, 0))
player_image = load_image('image\\player.png', (90, 90), (255, 255, 255))
enemy_image = load_image('image\\enemy.png', (100, 100), (0, 0, 0))

player = Player(400, 550, player_image, 6)

bullets = list()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.rect.centerx, player.rect.y, bullet_image, 10))

    player.update()
    for bullet in bullets:
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 

    window.blit(background, (0, 0))
    player.render(window)
    for bullet in bullets:
        bullet.render(window)
    pygame.display.update()
    clock.tick(FPS)