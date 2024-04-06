import pygame

class Alien(pygame.sprite.Sprite):
  def __init__(self, screen_hight, screen_width, x, y):
    super().__init__()
    self.image = pygame.image.load('./graphics/yellow.png').convert_alpha()
    self.rect = self.image.get_rect(midbottom = (x, y))
    self.speed = 2
    self.down_speed = 10
    self.screen_hight = screen_hight
    self.screen_width = screen_width
    self.direction = 'right'
  
  def update(self):
    self.movement()
    self.crossing_lines()

  def crossing_lines(self):
    if self.rect.x + self.rect.width >= self.screen_width: # touch to right
      self.rect.x -= self.speed
      self.rect.y += self.down_speed
      self.direction = 'left'
    elif self.rect.x <= 0: # touch to left
      self.rect.x += self.speed
      self.rect.y += self.down_speed
      self.direction = 'right'

  def movement(self):
    if self.direction == 'right':
      self.rect.x += self.speed
    else:
      self.rect.x -= self.speed

      