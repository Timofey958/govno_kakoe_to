import pygame

from src.sprite import Sprite

class EnemyKamikadze(Sprite):
    def update(self, player):
        self.rect.y += self.speed
        if self.rect.colliderect(player.rect):
            player.health -= 2

class EnemyShooting(Sprite):
    ...

class Boss(Sprite):
    ...
