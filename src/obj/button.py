import pygame
from src.config import BLACK

class Button(pygame.sprite.Sprite):
    def __init__(self, state, width, height, color, text) -> None:
        super().__init__()
        self.state = state
        self.group = state.group
        self.add(self.group)

        text_render = self.state.game.fonts["regular"].render(text, True, BLACK)

        if not width or not height:
            self.width, self.height = text_render.get_size()
            self.width += 20
            self.height += 20
        else:
            self.width, self.height = width, height

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(color)
        self.image.blit(text_render, (10, 10))

        self.rect = self.image.get_rect()

        self.pressed = False

    def action(self) -> None:
        pass

    def click_button(self) -> None:
        pygame.event.pump()
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            elif self.pressed:
                self.pressed = False
                self.action()
        else:
            self.pressed = False

    def update(self, actions) -> None:
        self.click_button()