import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, state, width, height) -> None:
        super().__init__()
        self.state = state
        self.group = state.group
        self.add(self.group)

        self.width = width
        self.height = height
        self.image = pygame.Surface([self.width, self.height])

        self.rect = self.image.get_rect()

    def action(self) -> None:
        pass