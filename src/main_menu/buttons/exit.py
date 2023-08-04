import pygame
from src.obj.button import Button
from src.config import RED, BLACK, WIDTH, HEIGHT

class ExitButton(Button):
    def __init__(self, state) -> None:
        super().__init__(state, WIDTH // 8, HEIGHT // 16)
        self.image.fill(RED)
        #self.image.blit(pygame.font.Font('./data/fonts/TNR.ttf', 30, bold=pygame.font.Font.bold).render("Exit Game", True, BLACK), (10, 10))

        self.rect.center = (WIDTH * 5 // 8, (HEIGHT * 2 // 3 + self.height * 2))

    def action(self) -> None:
        self.state.game.playing = False
        self.state.game.running = False

    def update(self, actions) -> None:
        self.click_button(None)