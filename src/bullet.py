import pygame

from src.sprite import Sprite

class Bullet(Sprite):
    def update(self, enemies):
        self.rect.y -= self.speed

class EnemyBullet(Sprite):
    def update(self, player):
        self.rect.y += self.speed

        if self.rect.colliderect(player.rect):
            player.health -= 1