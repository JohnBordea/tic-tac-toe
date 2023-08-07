from src.obj.screen import Screen
from src.main_menu.camera import Camera
from src.main_menu.buttons.exit import ExitButton
from src.main_menu.buttons.start import StartButton

class MainMenu(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.group = Camera(self.game.screen)

        StartButton(self)
        ExitButton(self)

    def update(self, delta_time, actions):
        self.group.update(delta_time, actions)

    def render(self, surface):
        self.group.draw()