import pygame
from scripts.player import Player



flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)

clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load('image\\background.png')
background = pygame.transform.scale(background, (800, 600))
bullet = pygame.image.load('image\\bullet.png')
player_image = pygame.image.load('image\\player.png')
player_image = pygame.transform.scale(player_image, (90, 90))
enemy_image = pygame.image.load('image\\enemy.png')

player = Player(400, 550, player_image, 6)



game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.update()

    window.blit(background, (0, 0))
    player.render(window)
    pygame.display.update()
    clock.tick(FPS)