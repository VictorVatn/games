from TwoKFourtyEight.funcs import *
import pygame
import random
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans', 80)
win = pygame.display.set_mode((708, 818))
win.fill((255, 255, 255))

board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
other_board = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

empty = []
for i in range(4):
    for col in range(4):
        if board[i][col] == 0:
            empty.append([i, col])
rand = empty[random.randrange(len(empty))]
row = rand[0]
col = rand[1]
num = 2
if random.randrange(10) == 9:
    num = 4
board[row][col] = num
other_board[row][col] = num

for row in range(4):
    for col in range(4):
        pygame.draw.rect(win, (238 + board[row][col], 228, 218), (12 * row + row * 162 + 12, 12 * col + col * 162 + 12 + 90, 162, 162))
        if board[row][col] > 0:
            text = font.render(str(board[row][col]), False, (0, 0, 0))
            win.blit(text, (12 * row + row * 162 + 12 + 50, 12 * col + col * 162 + 12 + 50 + 90))

run = True
while run:
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2] and 0 not in board[3]:
        if game_over(board):
            over = font.render("GAME OVER", False, (0, 0, 0))
            win.blit(over, (300, 400))
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        break

    pygame.time.delay(50)
    score = font.render("Score: " + str(sum(board[0]) + sum(board[1]) + sum(board[2]) + sum(board[3])), False, (0, 0, 0))
    pygame.draw.rect(win, (255, 255, 255), (0, 0, 698, 50))
    win.blit(score, (0, 0))
    keys = pygame.key.get_pressed()
    pygame.display.update()
    pygame.event.wait()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            break
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        if keys[pygame.K_UP]:
            board = left(board)
            if other_board == board:
                continue
            other_board = left(other_board)

        if keys[pygame.K_DOWN]:
            board = right(board)
            if other_board == board:
                continue
            other_board = right(other_board)

        if keys[pygame.K_LEFT]:
            board = up(board)
            if other_board == board:
                continue
            other_board = up(other_board)

        if keys[pygame.K_RIGHT]:
            board = down(board)
            if other_board == board:
                continue
            other_board = down(other_board)
    else:
        continue


    empty = []
    for i in range(4):
        for col in range(4):
            if board[i][col] == 0:
                empty.append([i, col])
    rand = empty[random.randrange(len(empty))]
    row = rand[0]
    col = rand[1]
    num = 2
    if random.randrange(10) == 9:
        num = 4
    board[row][col] = num
    other_board[row][col] = num

    for row in range(4):
        for col in range(4):
            try:
                pygame.draw.rect(win, (238, 228 - board[row][col], 218 - board[row][col]), (12 * row + row * 162 + 12, 12 * col + col * 162 + 12 + 90, 162, 162))
            except TypeError:
                pygame.draw.rect(win, (255, 0, 0),
                                 (12 * row + row * 162 + 12, 12 * col + col * 162 + 12 + 90, 162, 162))
            if board[row][col] > 0:
                text = font.render(str(board[row][col]), False, (0, 0, 0))
                win.blit(text, (12 * row + row * 162 + 12 + 50, 12 * col + col * 162 + 12 + 50 + 90))

pygame.quit()
