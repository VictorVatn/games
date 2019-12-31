from pong.classes import *
FPS = pygame.time.Clock()


def draw_window(ball, p1, p2):
    gameDisplay.fill(black)
    message_to_screen('Player1 Score:' + str(p1.score), white,  display_height // 2 - 18, (display_width // 2 - 100), "small")
    message_to_screen('Player2 Score:' + str(p2.score), white,  display_height // 2 - 18, -display_width // 2 + 100, "small")

    ball.draw(gameDisplay)
    p1.draw(gameDisplay)
    p2.draw(gameDisplay)
    pygame.display.update()


def game_over(ball, p1, p2):
    draw_window(ball, p1, p2)
    pygame.time.wait(500)
    game_loop(p1, p2, ball)


def message_to_screen(message, color, y_displace=0, x_displace=0, size="small"):
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = display_width // 2 - x_displace, display_height // 2 - y_displace
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, color, size):
    if size == 'small':
        textSurface = small_font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    elif size == 'med':
        textSurface = med_font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    elif size == 'large':
        textSurface = large_font.render(text, True, color)
        return textSurface, textSurface.get_rect()


def collision(p1x, p1y, p2x, p2y, ball):
    ball.coll_detect_wall()
    ball.coll_detect_player(p1x, p1y, p2x, p2y)


def key_getter_game(player1, player2, y_vel, player1_vel, player2_vel):
    p2_actions = 0
    p1_actions = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                pygame.quit()
                quit()

            if event.key == pygame.K_SPACE:
                pause()

            if event.key == pygame.K_UP and p2_actions == 0:
                player2_vel = -y_vel
                p2_actions = 1

            elif event.key == pygame.K_DOWN and p2_actions == 0:
                player2_vel = y_vel
                p2_actions = 1

            elif event.key == pygame.K_w and p1_actions == 0:
                player1_vel = -y_vel
                p1_actions = 1

            elif event.key == pygame.K_s and p1_actions == 0:
                player1_vel = y_vel
                p1_actions = 1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                if p2_actions == 1:
                    player2.move(player2_vel)
                player2_vel = -0

            elif event.key == pygame.K_DOWN:
                if p2_actions == 1:
                    player2.move(player2_vel)
                player2_vel = 0

            elif event.key == pygame.K_w:
                if p1_actions == 1:
                    player1.move(player1_vel)
                player1_vel = 0

            elif event.key == pygame.K_s:
                if p1_actions == 1:
                    player1.move(player1_vel)
                player1_vel = 0
    return y_vel, player1_vel, player2_vel


def pause():
    key_getter()


def key_getter():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


def win(winner):

    message_to_screen(winner + 'WINS!', white, 20, size='large')
    message_to_screen('Space to play again Q to quit', white, -50, size='small')
    pygame.display.update()

    key_getter()

    game_start()


def game_start():
    player1 = Player(0,
                     display_height / 2 - player_height / 2,
                     red,
                     player_width,
                     player_height,
                     display_height,
                     0)

    player2 = Player(display_width -
                     player_width,
                     display_height / 2 - player_height / 2,
                     red,
                     player_width,
                     player_height,
                     display_height,
                     0)

    ball = Ball(
        display_width // 2,
        display_height // 2,
        blue,
        ball_size
    )
    game_loop(player1, player2, ball)


def game_loop(player1, player2, ball):

    y_vel = 10
    player1_vel = 0
    player2_vel = 0

    pygame.time.wait(500)
    run = True

    draw_window(ball, player1, player2)

    while run:

        y_vel, player1_vel, player2_vel = key_getter_game(player1, player2, y_vel, player1_vel, player2_vel)

        player1.move(player1_vel)
        player2.move(player2_vel)
        ball.move()

        p1x, p1y = player1.coll_detect()
        p2x, p2y = player2.coll_detect()
        collision(p1x, p1y, p2x, p2y, ball)

        draw_window(ball, player1, player2)

        FPS.tick(15)
        over = ball.win_loss()

        if over:
            if ball.xvel > 0:
                player1.score += 1
            else:
                player2.score += 1

            if player1.score == 5 or player2.score == 5:

                draw_window(ball, player1, player2)

                if player1.score == 5:
                    player1.score = 0
                    player2.score = 0
                    win('PLAYER1')

                elif player2.score == 5:
                    player1.score = 0
                    player2.score = 0
                    win('PLAYER2')

            player2.x = display_width - player_width
            player2.y = display_height / 2 - player_height / 2

            player1.x = 0
            player1.y = display_height / 2 - player_height / 2

            ball.x = display_width // 2
            ball.y = display_height // 2
            game_over(ball, player1, player2)
