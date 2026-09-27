import pygame
from time import time
from random import randint

from src.player import Player
from src.config import *
from src.bullet import Bullet
from src.enemy import EnemyKamikadze

def main():
    windows = pygame.Window("bgegbrj", WIN_SIZE)
    surface = windows.get_surface()
    running = True
    clock = pygame.Clock()

    player_bullets = []
    kamikadze = []
    timer = time()
    timer_interval = 0.001

    backgroung_image = pygame.image.load("asssets/images.png")
    backgroung_image = pygame.transform.scale(backgroung_image, WIN_SIZE)

    player_image = pygame.image.load("asssets/player.png")
    player_image = pygame.transform.scale(player_image, [50, 50])

    bullet_image = pygame.image.load("asssets/bomba.png")
    bullet_image = pygame.transform.scale(bullet_image, [800, 400])

    kamikadze_image = pygame.image.load("asssets/kamikadze.png")
    kamikadze_image = pygame.transform.scale(kamikadze_image, [50, 50])

    player = Player((400, 500), player_image, 5)


    while running:
        # обработчик чето там то
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if event.button == 1:
                    center = player.rect.center
                    player_bullets.append(Bullet(center, bullet_image, BULLET_SPEED))

        if time() - timer >= timer_interval:
            timer += timer_interval 
            center = [
                randint(
                    kamikadze_image.get_width(),
                    WIN_WIDTH - kamikadze_image.get_width()
                    ),
                    -kamikadze_image.get_height()
                    ]
            kamikadze.append(EnemyKamikadze(center, kamikadze_image, KAMIKADZE_SPEED))

        player.update()
        print(kamikadze[0].rect if kamikadze else 0)

        for bullet in player_bullets:
            bullet.update([])
            if bullet.rect.bottom <= 0 or bullet.rect.top >= WIN_HEIGHT:
                player_bullets.remove(bullet)
            else:
                for kamikadzes in kamikadze:
                    if bullet.rect.colliderect(kamikadzes.rect):
                        kamikadze.remove(kamikadzes)

        for kamikadzes in kamikadze:
            kamikadzes.update(player)
            if kamikadzes.rect.top >= WIN_HEIGHT or kamikadzes.rect.colliderect(player.rect):
                kamikadze.remove(kamikadzes)

                
        surface.blit(backgroung_image)
        for bullet in player_bullets:
            bullet.render(surface)

        for kamikadzes in kamikadze:
            kamikadzes.render(surface)

        player.render(surface)
        windows.flip()

        clock.tick(MAX_FPS)
        # print(clock.get_fps())


if __name__ == "__main__":
    main()