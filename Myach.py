import pygame
SIZE = WIDTH, HEIGHT = 800, 600


class Board_ball():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 10

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x = self.left
        y = self.top
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            x = self.left
            y += self.cell_size


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    shar = Board_ball(11, 29)
    shar.set_view(shar.left, shar.top, shar.cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        screen.fill((0, 0, 0))
        shar.render(screen)
        pygame.display.flip()
    pygame.quit()