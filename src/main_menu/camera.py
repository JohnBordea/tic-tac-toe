import pygame
from src.config import WHITE

class Camera(pygame.sprite.Group):
    def __init__(self, screen) -> None:
        super().__init__()
        self.display_screen = screen

    def update(self, delta_time, actions) -> None:
        for sprite in self.sprites():
            sprite.update(actions)

    def draw(self):
        self.display_screen.fill(WHITE)

        for sprite in self.sprites():
            self.display_screen.blit(sprite.image, sprite.rect)