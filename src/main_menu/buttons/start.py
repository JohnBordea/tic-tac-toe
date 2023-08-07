from src.obj.button import Button
from src.config import GREEN, WIDTH, HEIGHT
from src.board.screen import BoardScreen

class StartButton(Button):
    def __init__(self, state) -> None:
        super().__init__(state, None, None, GREEN, "Start Game")

        self.rect.center = (WIDTH * 5 // 8, (HEIGHT * 2 // 3))

    def action(self) -> None:
        new_state = BoardScreen(self.state.game)
        new_state.enter_state()
        self.state.game.reset_keys()