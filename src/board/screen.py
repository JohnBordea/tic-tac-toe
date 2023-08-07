import pygame
from src.obj.screen import Screen
from src.board.camera import Camera

class BoardScreen(Screen):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.group = Camera(self.game.screen)

    def update(self, delta_time, actions):
        self.group.update(delta_time, actions)

    def render(self, surface):
        self.group.draw()
