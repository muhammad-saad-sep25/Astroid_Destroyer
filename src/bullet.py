import pygame
from settings import *

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y - 2, 10, 4)
        self.speed = BULLET_SPEED
        self.color = YELLOW

    def update(self):
        self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)