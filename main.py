import pygame
import random

from Myach import Board_ball
from pole_igrok import Board_player
from start_screen import start_screen

SIZE = WIDTH, HEIGHT = 800, 600
fps = 100


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    player = Board_player(3, 1)
    board = Board_ball(26, 63)
    button_pressed = pygame.USEREVENT + 1
    move_ball = pygame.USEREVENT + 2
    player.set_view(player.left, player.top, player.cell_size)
    board.set_view(board.left, board.top, board.cell_size)
    running = True
    flag = False
    board.create_ball()
    pygame.time.set_timer(move_ball, 50)
    start_screen(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == move_ball:
                board.move_ball()
                pygame.time.set_timer(move_ball, 0)
                pygame.time.set_timer(move_ball, 50)
            if event.type == button_pressed:
                for i in range(3):
                    player.board[0][i] = 0
                pygame.time.set_timer(button_pressed, 0)
                flag = False
            if event.type == pygame.KEYDOWN:
                if not flag:
                    key_pressed = player.get_click(event.key)
                    if key_pressed:
                        pygame.time.set_timer(button_pressed, 500)
                        flag = True
        if player.get_coords():
            if player.get_coords()[0] < board.get_coords()[0] < (player.get_coords()[0] + player.cell_size) and \
                 player.get_coords()[1] < board.get_coords()[1] < (player.get_coords()[1] + player.cell_size):
                if board.ball_flag:
                    board.ball_coords = (60, 3 + board.p_coord * 10)
                    board.ball_flag = False
                    board.a_coord = random.randint(0, 2)
        screen.fill((0, 0, 0))
        board.render(screen)
        player.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()