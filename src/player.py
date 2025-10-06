import pygame
import os
from settings import *
from bullet import Bullet

class Player:
    def __init__(self):
        self.image = pygame.image.load(os.path.join(PNGS_DIR, "player.png")).convert_alpha()
        self.rect = self.image.get_rect(center=(50, HEIGHT//4))
        self.speed = PLAYER_SPEED
        self.lives = 3
        self.bullets = []
        self.shoot_cooldown = 0
        self.shoot_sound = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "shoot.mp3"))

    def move(self, keys):
        if keys[pygame.K_w] and self.rect.top > 0: self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < HEIGHT: self.rect.y += self.speed
        if keys[pygame.K_a] and self.rect.left > 0: self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < WIDTH: self.rect.x += self.speed

    def shoot(self, keys):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        
        if keys[pygame.K_SPACE] and self.shoot_cooldown == 0:
            self.bullets.append(Bullet(self.rect.right, self.rect.centery))
            self.shoot_sound.play()
            self.shoot_cooldown = 15

    def update(self):
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.rect.left > WIDTH:
                self.bullets.remove(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)