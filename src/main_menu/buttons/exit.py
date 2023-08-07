from src.obj.button import Button
from src.config import RED, WIDTH, HEIGHT

class ExitButton(Button):
    def __init__(self, state) -> None:
        super().__init__(state, None, None, RED, "Exit Game")

        self.rect.center = (WIDTH * 5 // 8, (HEIGHT * 2 // 3 + self.height * 2))

    def action(self) -> None:
        self.state.game.playing = False
        self.state.game.running = False