import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, max_height):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = pos)
        self.speed = 10
        self.max_height = max_height

    def update(self):
        self.rect.y -= self.speed
        self.destroy()

    def destroy(self):
        if self.rect.y <= 0:
            self.kill()