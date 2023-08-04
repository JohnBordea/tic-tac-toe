import pygame
import sys
from src.game import Game

g = Game()
while g.running:
    g.game_loop()

pygame.quit()
sys.exit()