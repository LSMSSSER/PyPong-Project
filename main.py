import pygame

from Myach import Board_ball
from pole_igrok import Board_player

SIZE = WIDTH, HEIGHT = 800, 600
fps = 100


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    player = Board_player(3, 1)
    board = Board_ball(13, 29)
    button_pressed = pygame.USEREVENT + 1
    player.set_view(player.left, player.top, player.cell_size)
    board.set_view(board.left, board.top, board.cell_size)
    running = True
    flag = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == button_pressed:
                for i in range(3):
                    player.board[0][i] = 0
                #pygame.time.set_timer(button_pressed, 0)
                flag = False
            if event.type == pygame.KEYDOWN:
                if not flag:
                    key_pressed = player.get_click(event.key)
                    if key_pressed:
                        pygame.time.set_timer(button_pressed, 1000)
                        flag = True
        screen.fill((0, 0, 0))
        board.render(screen)
        player.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()