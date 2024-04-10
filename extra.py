import pygame

class Extra(pygame.sprite.Sprite):
  def __init__(self, screen_hight, screen_width,):
    super().__init__()
    self.image = pygame.image.load('./graphics/extra.png').convert_alpha()
    self.rect = self.image.get_rect(midbottom = (250, 50))
