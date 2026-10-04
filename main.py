import pygame
from time import time
from random import randint

from src.player import Player
from src.config import *
from src.bullet import Bullet
from src.enemy import EnemyKamikadze

def main():
    pygame.init()
    windows = pygame.Window("bgegbrj", WIN_SIZE)
    surface = windows.get_surface()
    running = True
    clock = pygame.Clock()

    pygame.mixer.music.load("asssets/background_music.mp3")
    pygame.mixer.music.play(-1)

    shoot_sound = pygame.mixer.Sound("asssets/shoot_sound.mp3")
    player_death_sound = pygame.mixer.Sound("asssets/shoot_sound.mp3")
    enemy_death_sound = pygame.mixer.Sound("asssets/shoot_sound.mp3")

    big_font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 32)


    player_bullets = []
    kamikadze = []
    timer = time()
    timer_interval = 0.1
    score = 0

    backgroung_image = pygame.image.load("asssets/images.png")
    backgroung_image = pygame.transform.scale(backgroung_image, WIN_SIZE)

    player_image = pygame.image.load("asssets/player.png")
    player_image = pygame.transform.scale(player_image, [50, 50])

    bullet_image = pygame.image.load("asssets/bomba.png")
    bullet_image = pygame.transform.scale(bullet_image, [10, 10])

    big_bullet_image = pygame.image.load("asssets/bomba.png")
    big_bullet_image = pygame.transform.scale(big_bullet_image, [800, 400])

 

    kamikadze_image = pygame.image.load("asssets/kamikadze.png")
    kamikadze_image = pygame.transform.scale(kamikadze_image, [50, 50])

    player = Player((400, 500), player_image, 5)


    while running:
        # обработчик чето там то
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shoot_sound.play()
                    center = player.rect.center
                    player_bullets.append(Bullet(center, bullet_image, BULLET_SPEED))
                if event.button == 3:
                    shoot_sound.play()
                    center = player.rect.center
                    player_bullets.append(Bullet(center, big_bullet_image, BULLET_SPEED))

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                player.health = PLAYER_MAX_HEALTH
                player.rect.center = [400, 500]
                player_bullets.clear()
                kamikadze.clear()
                score = 0
                # timer = time()
        
        if player.health > 0: 

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
            # print(kamikadze[0].rect if kamikadze else 0)

            for bullet in player_bullets:
                bullet.update([])
                if bullet.rect.bottom <= 0 or bullet.rect.top >= WIN_HEIGHT:
                    player_bullets.remove(bullet)
                else:
                    for kamikadzes in kamikadze:
                        if bullet.rect.colliderect(kamikadzes.rect):
                            kamikadze.remove(kamikadzes)
                            enemy_death_sound.play()
                            score += 10

            for kamikadzes in kamikadze:
                kamikadzes.update(player)
                if kamikadzes.rect.top >= WIN_HEIGHT or kamikadzes.rect.colliderect(player.rect):
                    kamikadze.remove(kamikadzes)
                if player.health <= 0:
                    player_death_sound.play()
                    # exit()

                
        surface.blit(backgroung_image)
        for bullet in player_bullets:
            bullet.render(surface)

        for kamikadzes in kamikadze:
            kamikadzes.render(surface)

        player.render(surface)

        txt_health = f"{player.health}|{PLAYER_MAX_HEALTH}"
        img_health = small_font.render(txt_health, True, "white")
        rect_health = img_health.get_rect(topleft=[20, 20])
        surface.blit(img_health, rect_health)

        txt_score = f"{score}"
        img_score = small_font.render(txt_score, True, "white")
        rect_score = img_health.get_rect(topright=[780, 20])
        surface.blit(img_score, rect_score)

        if player.health <= 0:
            rect = pygame.Rect(0, 0, 450, 300)
            rect.center = WIN_WIDTH / 2, WIN_HEIGHT / 2
            pygame.draw.rect(surface, "white", rect)

            txt_health = f"Чтобы начать заного\n нажмите R"
            img_health = big_font.render(txt_health, True, "red")
            rect_health = img_health.get_rect(center=rect.center)
            surface.blit(img_health, rect_health)
        
        windows.flip()

        clock.tick(MAX_FPS)
        # print(clock.get_fps())


if __name__ == "__main__":
    main()