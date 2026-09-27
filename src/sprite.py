import pygame

class Sprite:
    def __init__(self, center, image, speed):
        self.rect = pygame.FRect((0, 0), image.size)
        self.rect.center = center
        self.image = image
        self.speed = speed

    def render(self, surface):
        surface.blit(self.image, self.rect)