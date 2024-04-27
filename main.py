import pygame, sys
from player import Player
from alien import Alien
from extra import Extra
from tv import Tv

#스크린의 크기를 정하는 코드
screen_width, screen_hight = 500, 600
alien_num_in_row = 8
screen_magin = 50
row_distance = 50
score = 0
game_complete_surface_rect = 0
game_complete_surface = 0
die_signal = 0

pygame.init()

font = pygame.font.Font('./font/Pixeled.ttf', 20)

screen = pygame.display.set_mode((screen_width, screen_hight))
clock = pygame.time.Clock()
fps = 60

player_sprite = Player(screen_hight, screen_width)
player = pygame.sprite.GroupSingle(player_sprite)

# extra_sprite = Extra(screen_hight, screen_width)
# extra = pygame.sprite.Group(extra_sprite)

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
    # extra.update()
    # extra.draw(screen)
    space_invader_surface = font.render('space invader', True, 'white')
    space_invader_rect = space_invader_surface.get_rect(topleft = (0,-10))
    screen.blit(space_invader_surface, space_invader_rect)

    score_surface = font.render(str(score), True, 'white')
    score_rect = score_surface.get_rect(bottomright = (screen_width - 10, screen_hight - 10))
    screen.blit(score_surface, score_rect)

    tv_sprite.draw(screen)

    alien_hit = []

    for laser in player.sprite.lasers:
        alien_hit = pygame.sprite.spritecollide(laser, aliens, False)
        if len(alien_hit) >= 1:
            laser.kill()
            for alien in alien_hit:
                if alien.reduce_lives() == True:
                    score += len(alien_hit)
                

    # player_hit = pygame.sprite.spritecollide(aliens, player, False)
    # if player_hit:
    #     die_signal += 1

    if len(aliens.sprites()) == 0:
        screen.fill((30,30,30))
        game_complete_surface = font.render('game complete', True, 'white')
        game_complete_surface_rect = game_complete_surface.get_rect(midbottom = (screen_width - 250 , screen_hight - 300))
        screen.blit(game_complete_surface, game_complete_surface_rect)

    # if die_signal >= 1:
    #     screen.fill((160, 0, 0))
    #     game_over_surface = font.render('GameOver', True, 'black')
    #     game_over_surface_rect = game_over_surface.get_rect(midbottom = (screen_width - 250 , screen_hight - 300))
    #     screen.blit(game_over_surface, game_over_surface_rect)

    pygame.display.flip()
    clock.tick(fps)