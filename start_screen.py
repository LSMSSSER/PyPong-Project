def start_screen(screen):
    from main import WIDTH, HEIGHT
    import pygame

    clock = pygame.time.Clock()

    FPS = 50

    intro_text = ["Lofi Ping-pong",
                  "Все просто",
                  "Нужно всего лишь вовремя отбивать мячик песронажем",
                  "Нажимая соответсвующие кнопки",
                  '',
                  '',
                  '',
                  '',
                  'Настройки(пока не работает)']

    fon = pygame.transform.scale(pygame.image.load('fone.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('cyan'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)