import pygame
import random

pygame.init()
pygame.font.init()

small_font = pygame.font.SysFont("comicsansms", 25)
med_font = pygame.font.SysFont("comicsansms", 40)
large_font = pygame.font.SysFont("comicsansms", 70)

blue = (0, 50, 200)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


player_width = 15
player_height = 60
ball_size = 7

display_width = 1000
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))


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
    startx_vel = 15
    xvel = startx_vel
    yvel = 10
    if random.randint(0, 1) == 1:
        xvel *= -1
    if random.randint(0, 1) == 1:
        yvel *= -1

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
        if self.yvel < 0:
            if self.y + self.yvel <= 0:
                self.yvel *= -1

        else:
            if self.y + self.yvel >= self.display_height:
                self.yvel *= -1

    def coll_detect_player(self, player1x, player1y, player2x, player2y, player1_vel, player2_vel):

        if self.xvel < 0:
            if player1x <= self.x <= player1x + self.player_width * 2 or player1x <= self.x + self.radius <= player1x + self.player_width:
                if player1y <= self.y <= player1y + self.player_height or player1y <= self.y + self.radius <= player1y + self.player_height:
                    self.xvel = 25
                    if player1_vel > 0:
                        self.yvel = -10

                    elif player1_vel < 0:
                        self.yvel = 10

                    elif player1_vel == 0:
                        self.yvel = 0
                    self.yvel += round(((player1y + player_height / 2) - (self.y + self.radius)))


        else:
            if player2x <= self.x + self.radius * 2 <= player2x + self.player_width or player2x <= self.x + self.radius <= player2x + self.player_width:
                if player2y <= self.y <= player2y + self.player_height or player2y <= self.y + self.radius <= player2y + self.player_height:
                    self.xvel = -25

                    if player2_vel > 0:
                        self.yvel = -6

                    elif player2_vel < 0:
                        self.yvel = 6

                    elif player2_vel == 0:
                        self.yvel = 0
                    self.yvel += round(((player2y + player_height / 2) - (self.y + self.radius)))
        if self.yvel > 12:
            self.yvel = 12
        elif self.yvel < -12:
            self.yvel = -12

    def win_loss(self):
        if self.x + self.radius * 2 <= 0:
            return True
        elif self.x >= self.display_width:
            return True
        else:
            return False

    def move(self):
        self.x += self.xvel
        self.y += self.yvel

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
