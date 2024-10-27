import pygame
from scripts.player import Player
from scripts.functions import load_image
from scripts.bullet import Bullet
from scripts.enemy import Enemy
from time import time 
from random import randint

pygame.init()


flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((800, 600), flags)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)
big_font = pygame.font.Font(None, 64)

FPS = 60

bullets = list()

background = load_image('image', 'background.png', size=(800, 600), colorkey=None)
bullet_image = load_image('image', 'bullet.png', size=(35, 40), colorkey=(0, 0, 0))
player_image = load_image('image', 'player.png', size=(90, 90), colorkey=(255, 255, 255))
enemy_image = load_image('image', 'enemy.png', size=(100, 100), colorkey=(250, 250, 250))

player = Player(400, 550, player_image, 6, 3)

bullets = []
enemies = []

spawn_delta = 3.5
timer = time()
score = 0

game = True
died = False

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if died:
                score = 0
                died = False
                bullets.clear()
                enemies.clear()
                player.health = 3
                
                player.rect.center = (400, 550)
            if event.key == pygame.K_SPACE and not died:
                bullets.append(Bullet(player.rect.centerx, player.rect.y, bullet_image, 10))
    if not died:
        player.update()
        for bullet in bullets:
            bullet.update()
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet) 



        delta = time() - timer
        if delta > spawn_delta:
            timer = time()
            x = randint(enemy_image.get_width() // 2, 800 - enemy_image.get_width() // 2)
            y = - enemy_image.get_height() / 2
            speed = randint(5000, 7000) / 1000
            health = randint(1, 2 )
            enemies.append( Enemy(x, y, enemy_image, speed, health) )

        for enemy in enemies:
            enemy.update()
            
            for bullet in bullets:
                if enemy.is_collide(bullet):
                    bullets.remove(bullet)
                    enemy.get_damage()
            
            if enemy.is_collide(player):
                player.get_damage()
                enemies.remove(enemy)
                died = player.health <= 0

            elif enemy.health <= 0:
                score += 1
                enemies.remove(enemy)
                
    
    window.blit(background, (0, 0))
    player.render(window)
    for enemy in enemies:
        enemy.render(window)
    for bullet in bullets:
        bullet.render(window)
    
    text = 'Очки:' + str(score)
    image_text = font.render(text, True, (255, 255, 255))
    image_rect = image_text.get_rect(midtop = (400, 0))
    window.blit(image_text, image_rect) 
    
    text = 'Жизни:' + str(player.health)
    image_text = font.render(text, True, (255, 255, 255))
    image_rect = image_text.get_rect(topleft = (0, 0))
    window.blit(image_text, image_rect) 

    if died:
        text = 'YOU DIED!!!'
        image_text = big_font.render(text, True, (255, 50, 50))
        image_rect = image_text.get_rect(center=(400, 300))
        window.blit(image_text, image_rect)
        
        text = 'Нажмите любую конпку чтобы начать заново'
        image_text = font.render(text, True, (255, 255, 255))
        image_rect = image_text.get_rect(center=(400, 400))
        window.blit(image_text, image_rect)
         

    pygame.display.update()
    clock.tick(FPS)