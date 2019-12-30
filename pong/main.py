import pygame
from pong.classes import *

pygame.init()

blue = (0, 50, 200)
red = (255, 0, 0)
black = (0, 0, 0)


player_width = 10
player_height = 60
ball_size = 7

display_width = 1000
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(black)


def game_loop():
    p1 = Player(0, display_height / 2 - player_height / 2, red, player_width, player_height, display_height)
    p2 = Player(display_width - player_width, display_height / 2 - player_height / 2, red, player_width, player_height, display_height)

    FPS = pygame.time.Clock()

    y_vel = 10
    player1_vel = 0
    player2_vel = 0

    ball = Ball(display_width // 2, display_height // 2, blue, ball_size, display_width, display_height, player_width, player_height)

    run = True
    while run:
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

        gameDisplay.fill(black)

        ball.draw(gameDisplay)
        p1.draw(gameDisplay)
        p2.draw(gameDisplay)

        pygame.display.update()
        FPS.tick(15)


game_loop()
