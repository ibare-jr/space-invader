import pygame
from laser import Laser

class Alien(pygame.sprite.Sprite):
  def __init__(self, screen_hight, screen_width, x, y):
    super().__init__()
    self.image = pygame.image.load('./graphics/yellow.png').convert_alpha()
    self.rect = self.image.get_rect(midbottom = (x, y))
    self.speed = 2
    self.down_speed = self.rect.height + 5
    self.screen_hight = screen_hight
    self.screen_width = screen_width
    self.direction = 'right'
    self.lives = 2
    self.lasers = pygame.sprite.Group()

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

  def reduce_lives(self):
    self.lives -= 1
    if self.lives == 1: 
      self.image = pygame.image.load('./graphics/red.png').convert_alpha()
    if self.lives == 0:
      self.kill()
      return True
    else:
      return False
    
  def fire_laser(self):
    self.lasers.add(Laser(self.rect.center, self.screen_hight, 'down'))