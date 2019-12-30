import pygame
from pong.classes import *

pygame.init()
pygame.font.init()

small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 40)
large_font = pygame.font.SysFont("comicsansms", 70)

blue = (0, 50, 200)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


player_width = 10
player_height = 60
ball_size = 7

display_width = 1000
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))


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


def message_to_screen(message, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(message, color, size)
    textRect.center = display_width // 2, display_height // 2 - y_displace
    gameDisplay.blit(textSurf, textRect)


def game_over(p1, p2, ball):

    p1.draw(gameDisplay)
    p2.draw(gameDisplay)
    ball.draw(gameDisplay)
    message_to_screen('Space To Continue or Q To Quit', white, -50)
    pygame.display.update()

    game_exit = False
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def game_loop():
    p1 = Player(0, display_height / 2 - player_height / 2, red, player_width, player_height, display_height)
    p2 = Player(display_width - player_width, display_height / 2 - player_height / 2, red, player_width, player_height, display_height)

    FPS = pygame.time.Clock()

    y_vel = 10
    player1_vel = 0
    player2_vel = 0

    ball = Ball(display_width // 2, display_height // 2, blue, ball_size, display_width, display_height, player_width, player_height)

    gameDisplay.fill(black)
    ball.draw(gameDisplay)
    p1.draw(gameDisplay)
    p2.draw(gameDisplay)
    pygame.display.update()

    pygame.time.wait(500)
    over = False
    run = True
    while run:

        if over:
            game_over(p1, p2, ball)

        p1_actions = 0
        p2_actions = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

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
                        p2.move(player2_vel)
                    player2_vel = -0

                elif event.key == pygame.K_DOWN:
                    if p2_actions == 1:
                        p2.move(player2_vel)
                    player2_vel = 0

                elif event.key == pygame.K_w:
                    if p1_actions == 1:
                        p1.move(player1_vel)
                    player1_vel = 0

                elif event.key == pygame.K_s:
                    if p1_actions == 1:
                        p1.move(player1_vel)
                    player1_vel = 0

        p1.move(player1_vel)
        p2.move(player2_vel)
        p1x, p1y = p1.coll_detect()
        p2x, p2y = p2.coll_detect()
        ball.coll_detect(p1x, p1y, p2x, p2y)
        ball.move()
        over = ball.win_loss()

        gameDisplay.fill(black)

        ball.draw(gameDisplay)
        p1.draw(gameDisplay)
        p2.draw(gameDisplay)

        pygame.display.update()
        FPS.tick(15)


game_loop()
