import pygame

class Tv(pygame.sprite.Sprite):
  def __init__(self, screen_width, screen_hight):
    super().__init__()
    self.image = pygame.image.load('./graphics/tv.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (screen_width, screen_hight))
    self.screen_width = screen_width

  def draw(self, screen):
    self.image.set_alpha(75)
    self.make_lines()
    screen.blit(self.image, (0,0))

  def make_lines(self):
    line_distance = 3
    for line in range(30):
      pygame.draw.line(self.image, 'black', (0, line_distance), (self.screen_width, line_distance))
      line_distance += 20