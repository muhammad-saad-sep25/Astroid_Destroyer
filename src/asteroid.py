import pygame
import random
import os
from settings import *

class Asteroid:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(PNGS_DIR, "asteroid.png")).convert_alpha()
        size = random.randint(30, 70)
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(
            x=WIDTH,
            y=random.randint(0, HEIGHT - size)
        )
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)