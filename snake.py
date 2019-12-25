import pygame
import random
pygame.init()

img = pygame.image.load('snakehead.png')

FPS = 15

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 150, 0)

BLOCK_SIZE = 20

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()

small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 40)
large_font = pygame.font.SysFont("comicsansms", 70)


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
    # screen_text = font.render(message, True, color)
    # gameDisplay.blit(screen_text, [display_width // 2, display_height // 2])
    textRect.center = display_width // 2, display_height // 2 - y_displace
    gameDisplay.blit(textSurf, textRect)


def snake(block_size, snake_list, direction):
    global head

    for XnY in snake_list[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

    if direction == 'right':
        head = pygame.transform.rotate(img, 270)

    elif direction == 'up':
        head = img

    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)

    elif direction == 'left':
        head = pygame.transform.rotate(img, 90)

    gameDisplay.blit(head, (snake_list[-1][0], snake_list[-1][1]))


def game_loop():
    global actions_per_frame

    lead_x = display_width // 2
    lead_y = display_height // 2

    lead_x_change = 0
    lead_y_change = -BLOCK_SIZE
    direction = "up"

    apple_x = random.randrange(0, display_width - BLOCK_SIZE + 1, 20)
    apple_y = random.randrange(0, display_height - BLOCK_SIZE + 1, 20)

    snake_list = []
    snake_length = 1

    game_exit = False
    game_over = False
    while not game_exit:

        while game_over:

            gameDisplay.fill(black)
            snake(BLOCK_SIZE, snake_list, direction)
            message_to_screen("Game over", red, 50, "large")

            message_to_screen("Press Q to quit or Space to play again", white, -50, "med")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False

                    if event.key == pygame.K_SPACE:
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
                        direction = "left"
                        actions_per_frame += 1

                elif event.key == pygame.K_RIGHT:
                    if lead_x_change == 0:
                        lead_x_change = BLOCK_SIZE
                        lead_y_change = 0
                        direction = "right"
                        actions_per_frame += 1

                elif event.key == pygame.K_UP:
                    if lead_y_change == 0:
                        lead_y_change = -BLOCK_SIZE
                        lead_x_change = 0
                        direction = "up"
                        actions_per_frame += 1

                elif event.key == pygame.K_DOWN:
                    if lead_y_change == 0:
                        lead_y_change = BLOCK_SIZE
                        lead_x_change = 0
                        direction = "down"
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

        for segment in snake_list[1:-1]:
            if segment == snake_head:
                lead_x -= lead_x_change
                lead_y -= lead_y_change
                message_to_screen('You crashed into yourself', red)
                pygame.display.update()
                game_over = True
                continue

        if len(snake_list) > snake_length:
            del snake_list[0]

        snake(BLOCK_SIZE, snake_list, direction)

        if apple_x <= lead_x < apple_x + BLOCK_SIZE and apple_y <= lead_y < apple_y + BLOCK_SIZE:
            apple_x = random.randrange(0, display_width - BLOCK_SIZE + 1, 20)
            apple_y = random.randrange(0, display_height - BLOCK_SIZE + 1, 20)
            snake_length += 1

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


game_loop()
