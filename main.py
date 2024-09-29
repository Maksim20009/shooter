import pygame

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)

clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load('image\\background.png')
background = pygame.transform.scale(background, (800, 600))
bullet = pygame.image.load('image\\bullet.png')
player = pygame.image.load('image\\player.png')
enemy = pygame.image.load('image\\enemy.png')

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(FPS)