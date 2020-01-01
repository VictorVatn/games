from classes import *
FPS = pygame.time.Clock()

easy_coordinates = (30, 270, 100, 50)
easyX = easy_coordinates[0]
easyY = easy_coordinates[1]
easy_width = easy_coordinates[2]
easy_height = easy_coordinates[3]

medium_coordinates = (150, 270, 100, 50)
mediumX = medium_coordinates[0]
mediumY = medium_coordinates[1]
medium_width = medium_coordinates[2]
medium_height = medium_coordinates[3]

hard_coordinates = (270, 270, 100, 50)
hardX = hard_coordinates[0]
hardY = hard_coordinates[1]
hard_width = hard_coordinates[2]
hard_height = hard_coordinates[3]

normal_coordinates = (680, 270, 100, 50)
normalX = normal_coordinates[0]
normalY = normal_coordinates[1]
normal_width = normal_coordinates[2]
normal_height = normal_coordinates[3]

frantic_coordinates = (830, 270, 100, 50)
franticX = frantic_coordinates[0]
franticY = frantic_coordinates[1]
frantic_width = frantic_coordinates[2]
frantic_height = frantic_coordinates[3]


def homeScreen():

    gameDisplay.fill(black)
    message_to_screen('Pong', red, 110, size='large')
    message_to_screen("SinglePlayer", white, 100, 300, size='med')
    message_to_screen("TwoPlayer", white, 100, -300, size='med')

    pygame.display.update()

    intro = True
    while intro:

        button("Easy", easyX, easyY, easy_width, easy_height, light_green, green)
        button("Medium", mediumX, mediumY, medium_width, medium_height, light_yellow, yellow)
        button("Hard", hardX, hardY, hard_width, hard_height, light_red, red)

        button("Normal", normalX, normalY, normal_width, normal_height, light_green, green)
        button("Frantic", franticX, franticY, frantic_width, frantic_height, light_red, red)

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        FPS.tick(15)


def text_to_button(msg, color, buttonx, buttony, button_width, button_height):
    textSurf, textRect = text_objects(msg, color, "small")
    textRect.center = ((buttonx + button_width / 2),  buttony + button_height / 2)
    gameDisplay.blit(textSurf, textRect)


def button(text, x, y, width, height, active_color, inactive_color, text_color=black):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width >= mouse_pos[0] >= x and y + height >= mouse_pos[1] >= y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1:
            if text == 'Normal':
                game_start(2)
            else:
                if 'Frantic' != text:
                    game_start(1, text.lower())

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    text_to_button(text, text_color, x, y, width, height)


def message_to_screen(message, color, y_displace=0, x_displace=0, size="small"):
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = display_width // 2 - x_displace, display_height // 2 - y_displace
    gameDisplay.blit(textSurf, textRect)


def draw_window(ball, p1, p2):
    gameDisplay.fill(black)
    message_to_screen(str(p1.score), white,  display_height // 2 - 18, (display_width // 4), "small")
    message_to_screen(str(p2.score), white,  display_height // 2 - 18, -display_width // 4, "small")

    ball.draw(gameDisplay)
    p1.draw(gameDisplay)
    p2.draw(gameDisplay)
    pygame.display.update()


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


def collision(player1, player2, ball, player1_vel, player2_vel):
    ball.coll_detect_wall()
    ball.coll_detect_player(player1.x, player1.y, player2.x, player2.y, player1_vel, player2_vel)


def key_getter_game2player(player1, player2, player_vel):

    p2_actions = 0
    p1_actions = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                homeScreen()

            if event.key == pygame.K_SPACE:
                pause()

            if event.key == pygame.K_UP and p2_actions == 0:
                player2.vel = -player_vel
                p2_actions = 1

            elif event.key == pygame.K_DOWN and p2_actions == 0:
                player2.vel = player_vel
                p2_actions = 1

            elif event.key == pygame.K_w and p1_actions == 0:
                player1.vel = -player_vel
                p1_actions = 1

            elif event.key == pygame.K_s and p1_actions == 0:
                player1.vel = player_vel
                p1_actions = 1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                if p2_actions == 1:
                    player2.move()
                player2.vel = 0

            elif event.key == pygame.K_DOWN:
                if p2_actions == 1:
                    player2.move()
                player2.vel = 0

            elif event.key == pygame.K_w:
                if p1_actions == 1:
                    player1.move()
                player1.vel = 0

            elif event.key == pygame.K_s:
                if p1_actions == 1:
                    player1.move()
                player1.vel = 0


def restart(player1, player2, ball, scorer=''):
    player2.x = display_width - player_width * 2
    player2.y = display_height / 2 - player_height / 2

    player1.x = player_width
    player1.y = display_height / 2 - player_height / 2

    ball.x = display_width // 2
    ball.y = display_height // 2

    if random.randint(0, 1) == 1:
        ball.yVel = ball.starty_vel

    else:
        ball.yVel = -ball.starty_vel

    if scorer == 'player2':
        ball.xVel = -ball.startx_vel
    elif scorer == 'player1':
        ball.xVel = ball.startx_vel


def pause():
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
                    homeScreen()
        FPS.tick(15)


def win_player(winner, players, difficulty=''):

    message_to_screen(winner + ' WINS!', white, 20, size='large')
    message_to_screen('Space to play again Q to quit', white, -50, size='small')
    pygame.display.update()

    pause()

    if players == 2:
        game_start(2)

    else:
        game_start(1, difficulty)


def game_start(players, difficulty=''):
    player1 = Player(player_width,
                     display_height / 2 - player_height / 2,
                     red,
                     player_width,
                     player_height,
                     display_height,
                     0)

    player2 = Player(display_width -
                     player_width * 2,
                     display_height / 2 - player_height / 2,
                     red,
                     player_width,
                     player_height,
                     display_height,
                     0)

    ball = Ball(
        display_width // 2 + ball_size // 2,
        display_height // 2 + ball_size // 2,
        blue,
        ball_size,
        display_width,
        display_height,
        player_width,
        player_height)

    if players == 2:
        game_loop_2player(player1, player2, ball)
    else:
        if difficulty == 'easy':
            game_loop_1player(player1, player2, ball, easy)
        elif difficulty == 'medium':
            game_loop_1player(player1, player2, ball, medium)
        else:
            game_loop_1player(player1, player2, ball, hard)


def game_loop_2player(player1, player2, ball):

    player_speed = 10

    draw_window(ball, player1, player2)

    pygame.time.wait(500)
    run = True

    while run:
        FPS.tick(20)

        key_getter_game2player(player1, player2, player_speed)

        player1.move()
        player2.move()

        collision(player1, player2, ball, player1.vel, player2.vel)

        ball.move()

        draw_window(ball, player1, player2)

        over = ball.win_loss()

        if over:
            if ball.xVel > 0:
                player1.score += 1
                restart(player1, player2, ball, "player1")

            else:
                player2.score += 1
                restart(player1, player2, ball, "player2")

            if player1.score == 5 or player2.score == 5:

                draw_window(ball, player1, player2)

                if player1.score == 5:
                    player1.score = 0
                    player2.score = 0
                    win_player('PLAYER1', 2)

                elif player2.score == 5:
                    player1.score = 0
                    player2.score = 0
                    win_player('PLAYER2', 2)

            game_loop_2player(player1, player2, ball)


# One player version functions only from here onwards

def easy(player2, ball, player_speed):
    if player2.y + player_height // 2 > ball.y and ball.xVel > 0:
        player2.vel = -player_speed
        player2.move()

    elif player2.y + player_height // 2 < ball.y and ball.xVel > 0:
        player2.vel = player_speed
        player2.move()

    else:
        player2.vel = 0


def medium(player2, ball, player_speed):

    if ball.xVel > 0:

        if player2.y + player_height // 2 > ball.y:
            player2.vel = -player_speed
            player2.move()

        elif player2.y + player_height // 2 < ball.y:
            player2.vel = player_speed
            player2.move()

    else:
        if player2.y + player_height / 2 > display_height / 2:
            player2.vel = -player_speed
            player2.move()

        elif player2.y + player_height / 2 < display_height / 2:
            player2.vel = player_speed
            player2.move()


def hard(player2, ball, player_speed):

    if ball.xVel > 0:

        if ball.yVel > player_speed:
            if player2.y / 2.2 < ball.y and player2.x - ball.x > 60:
                player2.vel = player_speed
                player2.move()

            else:
                if player2.y + player_height / 2 > ball.y:
                    player2.vel = -player_speed

                elif player2.y + player_height / 2 < ball.y:
                    player2.vel = player_speed

        elif ball.yVel < -player_speed:
            if player2.y + player_height * 2.2 > ball.y and player2.x - ball.x > 60:
                player2.vel = -player_speed
                player2.move()

            else:
                if player2.y + player_height / 2 > ball.y:
                    player2.vel = -player_speed

                elif player2.y + player_height / 2 < ball.y:
                    player2.vel = player_speed

        else:
            if player2.y + player_height / 2 > ball.y:
                player2.vel = -player_speed
                player2.move()

            elif player2.y + player_height / 2 < ball.y:
                player2.vel = player_speed
                player2.move()

    else:
        if player2.y + player_height / 2 > display_height / 2:
            player2.vel = -player_speed
            player2.move()

        elif player2.y + player_height / 2 < display_height / 2:
            player2.vel = player_speed
            player2.move()


def key_getter_game_1player(player1, player_vel):

    p1_actions = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                homeScreen()

            if event.key == pygame.K_SPACE:
                pause()

            elif event.key == pygame.K_w or event.key == pygame.K_UP and p1_actions == 0:
                player1.vel = -player_vel
                p1_actions = 1

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN and p1_actions == 0:
                player1.vel = player_vel
                p1_actions = 1

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w or event.key == pygame.K_UP:
                if p1_actions == 1:
                    player1.move()
                player1.vel = 0

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if p1_actions == 1:
                    player1.move()
                player1.vel = 0


def game_loop_1player(player1, player2, ball, difficulty):

    player_speed = 10

    draw_window(ball, player1, player2)

    pygame.time.wait(500)

    run = True
    while run:
        FPS.tick(20)

        key_getter_game_1player(player1, player_speed)
        difficulty(player2, ball, player_speed)
        player1.move()

        collision(player1, player2, ball, player1.vel, player2.vel)

        ball.move()

        draw_window(ball, player1, player2)

        over = ball.win_loss()

        if over:
            if ball.xVel > 0:
                player1.score += 1
                restart(player1, player2, ball, "player1")
            else:
                player2.score += 1
                restart(player1, player2, ball, "player2")

            if player1.score == 5 or player2.score == 5:

                draw_window(ball, player1, player2)

                if player1.score == 5:
                    player1.score = 0
                    player2.score = 0
                    win_player('PLAYER1', 1, difficulty)

                elif player2.score == 5:
                    player1.score = 0
                    player2.score = 0
                    win_player('CPU', 1, difficulty)

            game_loop_1player(player1, player2, ball, difficulty)
