import pygame
from src.config import SQUARE_SIZE

class BoardData():
    def __init__(self) -> None:
        self.player = 1
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.game_over = None
        self.pressed = False
        self.mouse_coord= None

    def mark_square(self, row, col) -> None:
        self.board[row][col] = self.player

    def available_square(self, row, col) -> bool:
        return self.board[row][col] == 0

    def is_board_full(self) -> bool:
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 0:
                    return False

        return True

    def check_win(self):
        for col in range(3):
            if self.board[0][col] == self.player and self.board[1][col] == self.player and self.board[2][col] == self.player:
                self.game_over = ("col", col)
                return

        for row in range(3):
            if self.board[row][0] == self.player and self.board[row][1] == self.player and self.board[row][2] == self.player:
                self.game_over = ("row", row)
                return

        if self.board[2][0] == self.player and self.board[1][1] == self.player and self.board[0][2] == self.player:
            self.game_over = ("diag", 1)
            return

        if self.board[0][0] == self.player and self.board[1][1] == self.player and self.board[2][2] == self.player:
            self.game_over = ("diag", 2)
            return

        if self.is_board_full():
            self.game_over = ("draw")
            return

    def reset(self):
        self.player = 1
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.game_over = None

    def action(self):
        if self.mouse_coord:
            clicked_row = int(self.mouse_coord[1] // SQUARE_SIZE)
            clicked_col = int(self.mouse_coord[0] // SQUARE_SIZE)
            if self.available_square( clicked_row, clicked_col ):
                self.mark_square( clicked_row, clicked_col)
                self.check_win()
                self.player = 1 if self.player == 2 else 2
            self.mouse_coord = None

    def update(self, actions):
        if actions['reset']:
            self.reset()
            return
        if not self.game_over:
            pygame.event.pump()
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
                self.mouse_coord = pygame.mouse.get_pos()
            elif self.pressed:
                self.pressed = False
                self.action()