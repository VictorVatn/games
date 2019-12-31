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


player_width = 10
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

    def increase_point(self):
        self.score += 1


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

    def coll_detect_wall(self):
        if self.YVEL < 0:
            if self.y + self.YVEL <= 0:
                self.YVEL *= -1

        else:
            if self.y + self.YVEL >= self.game_height:
                self.YVEL *= -1

    def coll_detect_player(self, player1x, player1y, player2x, player2y):

        if self.XVEL < 0:
            if player1x < self.x <= player1x + self.player_width or player1x < self.x + self.radius * 2 < player1x:
                if player1y < self.y < player1y + self.player_height or player1y < self.x + self.radius * 2 < player1y:
                    self.XVEL *= -1
        elif self.XVEL > 0:
            if player2x < self.x + self.radius <= player2x + self.player_width or player2x < self.x + self.radius + self.radius * 2 < player2x:
                if player2y < self.y < player2y + self.player_height or player2y < self.radius * 2 < player2y + self.player_height:
                    self.XVEL *= -1

    def win_loss(self):
        if self.x + self.radius * 2 <= 0:
            return True
        elif self.x >= self.game_width:
            return True
        else:
            return False

    def move(self):
        self.x += self.XVEL
        self.y += self.YVEL

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
