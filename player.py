import pygame
from laser import Laser

class Player(pygame.sprite.Sprite):
  def __init__(self, screen_hight, screen_width):
    super().__init__()
    self.image = pygame.image.load('./graphics/player.png').convert_alpha()
    self.rect = self.image.get_rect(midbottom = (250, 500))
    self.rect = self.image.get_rect(midbottom = (300, 500))
    self.speed = 10
    self.laser_sound = pygame.mixer.Sound('./audio/laser.wav')
    self.laser_sound.set_volume(0.1)
    self.lasers = pygame.sprite.Group()
    self.screen_hight = screen_hight
    self.screen_width = screen_width
    self.laser_time = 0
    self.laser_cooltime = 100
    self.laser_fire = False

  def update(self):
    self.handle_keyboard()
    self.crossing_lines()
    self.lasers.update()

  def handle_keyboard(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rect.x -= self.speed
    elif keys[pygame.K_RIGHT]:
      self.rect.x += self.speed
    elif keys[pygame.K_SPACE]:
      if self.laser_fire == False:
        self.laser_sound.play()
        self.lasers.add(Laser(self.rect.center, self.screen_hight))
        self.laser_fire = True
        self.laser_time = pygame.time.get_ticks()
    if self.laser_fire == True:
      current_time = pygame.time.get_ticks()
      if current_time - self.laser_time >= self.laser_cooltime:
        self.laser_fire = False

  def crossing_lines(self):
    if self.rect.x + self.rect.width >= self.screen_width:
      self.rect.x -= self.speed
    elif self.rect.x <= 0:
      self.rect.x += self.speed
    