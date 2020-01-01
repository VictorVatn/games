import pygame
import random

pygame.init()
pygame.font.init()

small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 40)
large_font = pygame.font.SysFont("comicsansms", 70)

blue = (0, 50, 200)
red = (240, 0, 0)
light_red = (255, 40, 40)

black = (0, 0, 0)
white = (255, 255, 255)

green = (14, 201, 52)
light_green = (14, 255, 52)

yellow = (230, 230, 0)
light_yellow = (255, 255, 100)

player_width = 10
player_height = 60
ball_size = 7

display_width = 1000
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PONG ULTIMATE')


class Player:

    def __init__(self, x, y, color, width, height, display_height, score):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.display_height = display_height
        self.score = score
        self.vel = 0

    def move(self):
        move_or_not = True
        move_or_not2 = True

        if self.display_height <= self.y + self.height and self.vel > 0:
            move_or_not = False

        if 0 >= self.y and self.vel < 0:
            move_or_not2 = False

        if not move_or_not or not move_or_not2:
            self.vel = 0
        self.y += self.vel

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])


class Ball:
    max_yvel = 14
    starty_vel = 10
    startx_vel = 12
    xVel = startx_vel
    yVel = 10
    if random.randint(0, 1) == 1:
        xVel *= -1
    if random.randint(0, 1) == 1:
        yVel *= -1

    def __init__(self, x, y, color, radius, display_width, display_height, player_width, player_height):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.display_height = display_height
        self.player_width = player_width
        self.player_height = player_height
        self.display_width = display_width

    def coll_detect_wall(self):
        if self.y + self.yVel <= 0:
            self.yVel *= -1

        elif self.y + self.yVel >= self.display_height:
            self.yVel *= -1

    def coll_detect_player(self, player1x, player1y, player2x, player2y, player1_vel, player2_vel):

        if self.xVel < 0:
            if 0 <= self.x + self.xVel <= player1x + self.player_width:
                if player1y <= self.y <= player1y + self.player_height or player1y <= self.y + self.radius * 2 <= player1y + self.player_height:
                    self.xVel = 20
                    self.x = player1x + self.player_width - self.xVel + self.radius

                    if player1_vel > 0:
                        self.yVel = -8

                    elif player1_vel < 0:
                        self.yVel = 8

                    elif player1_vel == 0:
                        self.yVel = 0
                    self.yVel += round(((player1y + player_height / 2) - (self.y + self.radius)) / 3)

        else:
            if player2x <= self.x + self.radius * 2 + self.xVel:
                if player2y <= self.y <= player2y + self.player_height or player2y <= self.y + self.radius * 2 <= player2y + self.player_height:
                    self.xVel = -20
                    self.x = player2x - self.xVel - self.radius

                    if player2_vel > 0:
                        self.yVel = -10

                    elif player2_vel < 0:
                        self.yVel = 10

                    elif player2_vel == 0:
                        self.yVel = 0
                    self.yVel += round(((player2y + player_height / 2) - (self.y + self.radius)) / 3)

        if self.yVel > self.max_yvel:
            self.yVel = self.max_yvel
        elif self.yVel < -self.max_yvel:
            self.yVel = -self.max_yvel

    def win_loss(self):
        if self.x + self.radius * 2 <= 0:
            return True
        elif self.x >= self.display_width:
            return True
        else:
            return False

    def move(self):
        self.x += self.xVel
        self.y += self.yVel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
