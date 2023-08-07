import pygame
from src.config import WHITE, BLACK, LINE_WIDTH, SQUARE_SIZE, WIDTH, HEIGHT, CIRCLE_RADIUS, SPACE
from src.board.board import BoardData

class Camera(pygame.sprite.Group):
    def __init__(self, screen) -> None:
        super().__init__()
        self.display_screen = screen

        self.lines = [
            ( (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE) ),
            ( (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE) ),
            ( (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT) ),
            ( (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT) )
        ]

        self.board = BoardData()

    def _draw_board_lines(self):
        pygame.draw.line(self.display_screen, BLACK, self.lines[0][0], self.lines[0][1], LINE_WIDTH )
        pygame.draw.line(self.display_screen, BLACK, self.lines[1][0], self.lines[1][1], LINE_WIDTH )
        pygame.draw.line(self.display_screen, BLACK, self.lines[2][0], self.lines[2][1], LINE_WIDTH )
        pygame.draw.line(self.display_screen, BLACK, self.lines[3][0], self.lines[3][1], LINE_WIDTH )

    def _draw_cross(self, x, y):
        pygame.draw.line(self.display_screen, BLACK, (y * SQUARE_SIZE + SPACE, x * SQUARE_SIZE + SQUARE_SIZE - SPACE), (y * SQUARE_SIZE + SQUARE_SIZE - SPACE, x * SQUARE_SIZE + SPACE), LINE_WIDTH )
        pygame.draw.line(self.display_screen, BLACK, (y * SQUARE_SIZE + SPACE, x * SQUARE_SIZE + SPACE), (y * SQUARE_SIZE + SQUARE_SIZE - SPACE, x * SQUARE_SIZE + SQUARE_SIZE - SPACE), LINE_WIDTH )

    def _draw_circle(self, x, y):
        pygame.draw.circle(self.display_screen, BLACK, (int(y * SQUARE_SIZE + SQUARE_SIZE//2 ), int(x * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, LINE_WIDTH )

    def _draw_vertical_winning_line(self, col):
        posX = col * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.line(self.display_screen, BLACK, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

    def _draw_horizontal_winning_line(self, row):
        posY = row * SQUARE_SIZE + SQUARE_SIZE//2
        pygame.draw.line(self.display_screen, BLACK, (15, posY), (WIDTH - 15, posY), LINE_WIDTH )

    def _draw_asc_diagonal(self):
        pygame.draw.line(self.display_screen, BLACK, (15, HEIGHT - 15), (WIDTH - 15, 15), LINE_WIDTH )

    def _draw_desc_diagonal(self):
        pygame.draw.line(self.display_screen, BLACK, (15, 15), (WIDTH - 15, HEIGHT - 15), LINE_WIDTH )

    def update(self, delta_time, actions) -> None:
        self.board.update(actions)

    def draw(self):
        self.display_screen.fill(WHITE)

        self._draw_board_lines()

        for i, x in enumerate(self.board.board):
            for j, y in enumerate(x):
                if y == 1:
                    self._draw_circle(i, j)
                elif y == 2:
                    self._draw_cross(i, j)

        if self.board.game_over:
            if self.board.game_over[0] == "col":
                self._draw_vertical_winning_line(self.board.game_over[1])
            elif self.board.game_over[0] == "row":
                self._draw_horizontal_winning_line(self.board.game_over[1])
            elif self.board.game_over[0] == "diag" and self.board.game_over[1] == 1:
                self._draw_asc_diagonal()
            elif self.board.game_over[0] == "diag" and self.board.game_over[1] == 2:
                self._draw_desc_diagonal()