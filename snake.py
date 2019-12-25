import pygame
import random
pygame.init()

FPS = 15

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 150, 0)

BLOCK_SIZE = 10

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 20)


def message_to_screen(message, color):
    screen_text = font.render(message, True, color)
    gameDisplay.blit(screen_text, [display_width // 2, display_height // 2])
    pygame.display.update()


def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def game_loop():

    global actions_per_frame
    lead_x = display_width // 2
    lead_y = display_height // 2

    lead_x_change = 0
    lead_y_change = -BLOCK_SIZE

    apple_x = round(random.randint(0, display_width - BLOCK_SIZE) / 10) * 10
    apple_y = round(random.randint(0, display_height - BLOCK_SIZE) / 10) * 10

    snake_list = []
    snake_length = 1

    game_exit = False
    game_over = False
    while not game_exit:

        while game_over:

            gameDisplay.fill(black)
            pygame.draw.rect(gameDisplay, green, [lead_x, lead_y, BLOCK_SIZE, BLOCK_SIZE])
            message_to_screen("Game over, press C to play again or Q to quit", white)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False

                    if event.key == pygame.K_c:
                        game_loop()

        actions_per_frame = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN and actions_per_frame == 0:
                if event.key == pygame.K_LEFT:
                    if lead_x_change == 0:
                        lead_x_change = -BLOCK_SIZE
                        lead_y_change = 0
                        actions_per_frame += 1

                elif event.key == pygame.K_RIGHT:
                    if lead_x_change == 0:
                        lead_x_change = BLOCK_SIZE
                        lead_y_change = 0
                        actions_per_frame += 1

                elif event.key == pygame.K_UP:
                    if lead_y_change == 0:
                        lead_y_change = -BLOCK_SIZE
                        lead_x_change = 0
                        actions_per_frame += 1

                elif event.key == pygame.K_DOWN:
                    if lead_y_change == 0:
                        lead_y_change = BLOCK_SIZE
                        lead_x_change = 0
                        actions_per_frame += 1

        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            lead_x -= lead_x_change
            lead_y -= lead_y_change
            game_over = True
            continue

        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)

        for segment in snake_list[:-1]:
            if segment == snake_head:
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                message_to_screen('You crashed into yourself', red)
                game_over = True
                continue

        if len(snake_list) > snake_length:
            del snake_list[0]

        snake(BLOCK_SIZE, snake_list)

        if apple_x <= lead_x < apple_x + BLOCK_SIZE and apple_y <= lead_y < apple_y + BLOCK_SIZE:
            apple_x = round(random.randint(0, display_width - BLOCK_SIZE) / 10) * 10
            apple_y = round(random.randint(0, display_height - BLOCK_SIZE) / 10) * 10
            snake_length += 1

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


game_loop()
