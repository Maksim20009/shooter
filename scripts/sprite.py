class Sprite():
    def __init__(self, x, y, image, speed):
        self.image = image
        self.rect = image.get_rect(center=(x, y))
        self.speed = speed

    def is_collide(self, enemy):
        return self.rect.colliderect(enemy.rect)

    def render(self, window):
        window.blit(self.image, self.rect)
