import pygame
import random
pygame.init()


class Player:

    def __init__(self, x, y, color, width, height, display_height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.display_height = display_height

    def move(self, vel):
        move_or_not = True
        move_or_not2 = True

        if self.display_height <= self.y + self.height and vel > 0:
            move_or_not = False

        if 0 >= self.y and vel < 0:
            move_or_not2 = False

        if move_or_not and move_or_not2:
            self.y += vel

    def coll_detect(self):
        return self.x, self.y

    def draw(self, win):
        pygame.draw.rect(win, self.color, [self.x, self.y, self.width, self.height])


class Ball:
    XVEL = 14
    YVEL = 10
    if random.randint(0, 1) == 1:
        XVEL *= -1
    if random.randint(0, 1) == 1:
        YVEL *= -1

    def __init__(self, x, y, color, radius, game_width, game_height, player_width, player_height):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.game_width = game_width
        self.game_height = game_height
        self.player_width = player_width
        self.player_height = player_height

    def coll_detect(self, player1x, player1y, player2x, player2y):
        if self.YVEL < 0:
            if self.y + self.YVEL <= 0:
                self.YVEL *= -1

        else:
            if self.y + self.YVEL >= self.game_height:
                self.YVEL *= -1

        if self.XVEL < 0:
            if player1x < self.x <= player1x + self.player_width or player1x < self.x + self.radius * 2 < player1x:
                if player1y < self.y < player1y + self.player_height or player1y < self.x + self.radius * 2 < player1y:
                    self.XVEL *= -1
        elif self.XVEL > 0:
            if player2x < self.x + self.radius <= player2x + self.player_width or player2x < self.x + self.radius + self.radius * 2 < player2x:
                if player2y < self.y < player2y + self.player_height or player2y < self.radius * 2 < player2y + self.player_height:
                    self.XVEL *= -1

    def move(self):
        self.x += self.XVEL
        self.y += self.YVEL

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

