from .sprite import Sprite
import pygame
class Player(Sprite):
    def __init__(self, x, y, image, speed, health):
        super().__init__(x, y, image, speed)
        self.health = health

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed


    def get_damage(self):
        self.health -= 1