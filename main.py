import pygame, sys
from player import Player
from alien import Alien
from tv import Tv

#스크린의 크기를 정하는 코드
screen_width, screen_hight = 500, 600
alien_num_in_row = 8
screen_magin = 50
row_distance = 50

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()
fps = 60

player_sprite = Player(screen_hight, screen_width)
player = pygame.sprite.GroupSingle(player_sprite)

aliens = pygame.sprite.Group()
alien_start_pos = []

for line in range(5):
    for count in range(alien_num_in_row):
        alien_start_pos.append([screen_magin + (count * ((screen_width - (screen_magin * 2)) / alien_num_in_row)), 100 + (row_distance * line)])

for position in alien_start_pos:
    alien_sprite_1 = Alien(screen_hight, screen_width, position[0], position[1])
    aliens.add(alien_sprite_1)

tv_sprite = Tv(screen_width, screen_hight)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((30, 30, 30))

    player.update()
    player.sprite.lasers.draw(screen)    
    player.draw(screen)
    aliens.update()
    aliens.draw(screen)
    tv_sprite.draw(screen)

    for laser in player.sprite.lasers:
        if pygame.sprite.spritecollide(laser, aliens, True):
            laser.kill()

    pygame.display.flip()
    clock.tick(fps)