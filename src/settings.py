import os
import pygame

# Screen
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Goes up to root
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
PNGS_DIR = os.path.join(ASSETS_DIR, "Pngs")  # Note uppercase 'P'
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

# Gameplay
PLAYER_SPEED = 5
BULLET_SPEED = 7
ASTEROID_SPAWN_RATE = 45