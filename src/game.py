import pygame, time
from src.config import WIDTH, HEIGHT, FPS
from src.main_menu.screen import MainMenu

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.clock = pygame.time.Clock()
        self.fonts = {
            "regular": pygame.font.Font('./data/fonts/TNR.ttf', 30),
            "bald":    pygame.font.Font('./data/fonts/TNR.ttf', 30, bold=pygame.font.Font.bold)
        }
        self.running, self.playing = True, True
        self.dt, self.prev_time = 0, 0
        self.state_stack = []

        self.actions = {
            "reset": False
        }
        self.load_states()

    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_r:
                    self.actions['reset'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_r:
                    self.actions['reset'] = False

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.screen)
        pygame.display.flip()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def load_states(self):
        self.title_screen = MainMenu(self)
        self.state_stack.append(self.title_screen)