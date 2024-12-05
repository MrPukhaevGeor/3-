import pygame
from Board import Board


if __name__ == '__main__':
    pygame.init()
    board = Board(5, 7)
    screen = pygame.display.set_mode((5 * board.cell_size + board.left * 2, 7 * board.cell_size + board.top * 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()