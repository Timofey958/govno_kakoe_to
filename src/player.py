import pygame

from src.config import WIN_WIDTH, PLAYER_MAX_HEALTH
from src.sprite import Sprite

class Player(Sprite):
    def __init__(self, center, image, speed):
        super().__init__(center, image, speed)
        self.health = PLAYER_MAX_HEALTH

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        