import pygame
import random
import os
from settings import *
from player import Player
from asteroid import Asteroid

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.reset_game()

    def reset_game(self):
        self.player = Player()
        self.asteroids = []
        self.spawn_timer = 0
        self.wave = 1
        self.score = 0
        self.wave_start_time = pygame.time.get_ticks()
        pygame.mixer.music.load(os.path.join(SOUNDS_DIR, "Music.mp3"))
        pygame.mixer.music.play(-1)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def spawn_asteroids(self):
        self.spawn_timer += 1
        if self.spawn_timer > ASTEROID_SPAWN_RATE - (self.wave * 2):
            self.asteroids.append(Asteroid())
            self.spawn_timer = 0

    def check_collisions(self):
        for asteroid in self.asteroids[:]:
            # Player collision
            if self.player.rect.colliderect(asteroid.rect):
                self.asteroids.remove(asteroid)
                self.player.lives -= 1
                explosion = pygame.mixer.Sound(os.path.join(SOUNDS_DIR, "Explosion.mp3"))
                explosion.play()
                if self.player.lives <= 0:
                    self.game_over()
            
            # Bullet collisions
            for bullet in self.player.bullets[:]:
                if bullet.rect.colliderect(asteroid.rect):
                    self.asteroids.remove(asteroid)
                    self.player.bullets.remove(bullet)
                    self.score += 10
                    break

    def update_wave(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.wave_start_time) // 1000 > 30:  # 30 seconds per wave
            self.wave += 1
            self.wave_start_time = current_time

    def game_over(self):
        print(f"Game Over! Final Score: {self.score}")
        self.reset_game()

    def draw_ui(self):
        lives_text = self.font.render(f"Lives: {self.player.lives}", True, WHITE)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        wave_text = self.font.render(f"Wave: {self.wave}", True, WHITE)
        
        self.screen.blit(lives_text, (10, 10))
        self.screen.blit(score_text, (10, 40))
        self.screen.blit(wave_text, (10, 70))

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            
            # Update
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.player.shoot(keys)
            self.player.update()
            
            self.spawn_asteroids()
            for asteroid in self.asteroids:
                asteroid.update()
                if asteroid.rect.right < 0:
                    self.asteroids.remove(asteroid)
            
            self.check_collisions()
            self.update_wave()
            
            # Draw
            self.screen.fill(BLACK)
            for asteroid in self.asteroids:
                asteroid.draw(self.screen)
            self.player.draw(self.screen)
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()