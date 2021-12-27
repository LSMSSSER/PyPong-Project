import pygame
import random
SIZE = WIDTH, HEIGHT = 800, 600


class Board_ball:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 360
        self.top = 165
        self.cell_size = 5
        self.ball_coords = None
        self.ball_flag = True
        self.k = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        x = self.left
        y = self.top
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j] = 0
        if self.ball_coords:
            self.board[self.ball_coords[0]][self.ball_coords[1]] = 1
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size))
                x += self.cell_size
            x = self.left
            y += self.cell_size

    def get_coords(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    return (self.top + self.cell_size * i, self.left + self.cell_size * j)

    def create_ball(self):
        self.ball_coords = (0, 13)
        self.a_coord = 1
        self.p_coord = random.randint(0, 2)

    def move_ball(self):
        if self.ball_coords[0] == 0 and not self.ball_flag:
            self.ball_flag = True
            self.p_coord = random.randint(0, 2)
        if self.p_coord - self.a_coord == 0:
            if self.ball_flag:
                self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1])
            else:
                self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1])
        elif abs(self.p_coord - self.a_coord) == 1:
            if self.ball_flag:
                if self.p_coord > self.a_coord:
                    if self.k < 5:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1] + 1)
                        self.k = 0
                else:
                    if self.k < 5:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1] - 1)
                        self.k = 0
            else:
                if self.p_coord > self.a_coord:
                    if self.k < 5:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1] - 1)
                        self.k = 0
                else:
                    if self.k < 5:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1] + 1)
                        self.k = 0
        else:
            if self.ball_flag:
                if self.p_coord > self.a_coord:
                    if self.k < 2:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1] + 1)
                        self.k = 0
                else:
                    if self.k < 2:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] + 1, self.ball_coords[1] - 1)
                        self.k = 0
            else:
                if self.p_coord > self.a_coord:
                    if self.k < 2:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1] - 1)
                        self.k = 0
                else:
                    if self.k < 2:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1])
                        self.k += 1
                    else:
                        self.ball_coords = (self.ball_coords[0] - 1, self.ball_coords[1] + 1)
                        self.k = 0
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