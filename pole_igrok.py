import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600



class Board_player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 360
        self.top = 450
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x = self.left
        y = self.top
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                x += self.cell_size + 20
            x = self.left
            y += self.cell_size

    def get_click(self, key):
        if key == pygame.K_LEFT:
            arrow = 1
        elif key == pygame.K_RIGHT:
            arrow = 3
        elif key == pygame.K_UP:
            arrow = 2
        else:
            return None
        self.on_click(arrow)
        return arrow

    def on_click(self, arrow):
        if arrow == 1:
            self.board[0][0] = 1
        elif arrow == 2:
            self.board[0][1] = 1
        elif arrow == 3:
            self.board[0][2] = 1

    def get_coords(self):
        for i in range(3):
            if self.board[0][i] == 1:
                return(self.top, self.left + (self.cell_size + 20) * i)
        return None


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    shar = Board_player(3, 1)
    shar.set_view(shar.left, shar.top, shar.cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                shar.get_click(event.key)
        screen.fill((0, 0, 0))
        shar.render(screen)
        pygame.display.flip()
    pygame.quit()