import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for h in range(self.width):
            for w in range(self.height):
                if self.board[w][h]:
                    pygame.draw.rect(screen, 'white', (
                    self.left + h * self.cell_size, self.top + w * self.cell_size, self.cell_size, self.cell_size), 0)
                else:
                    pygame.draw.rect(screen, 'white', (
                        self.left + h * self.cell_size, self.top + w * self.cell_size, self.cell_size, self.cell_size),
                                     1)

    def get_cell(self, mouse_pos):
        col = (mouse_pos[0] - self.left + self.cell_size - 1) // self.cell_size
        row = (mouse_pos[1] - self.left + self.cell_size - 1) // self.cell_size
        if col >= 0 and col < self.width and row >= 0 and row < self.height:
            return row, col
        return None

    def on_click(self, cell):
        row = cell[0] - 1
        for i in range(self.width):
            self.board[row][i] = (self.board[row][i] + 1) % 2
        col = cell[1] - 1
        for i in range(self.height):
            self.board[i][col] = (self.board[i][col] + 1) % 2
        self.board[row][col] = (self.board[row][col] + 1) % 2

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(f'({cell[0] - 1}, {cell[1] - 1})')
        if cell:
            self.on_click(cell)

