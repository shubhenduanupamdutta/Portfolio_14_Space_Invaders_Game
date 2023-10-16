import pygame as pg
from random import randint, choice

import pygame.event

# CONSTANTS
WIDTH = 800
HEIGHT = 600


class Student(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((30, 40))
        self.image.fill(pg.Color('dodgerblue1'))
        self.rect = self.image.get_rect(center=(320, 240))
        self.speed = 5


# Initializing pygame engine
pg.init()

# General
# screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Student's Life")
# timer
clock = pg.time.Clock()
# fonts
font_normal = pg.font.Font('font/Action_Man.ttf', 24)
font_large = pg.font.Font('font/Action_Man.ttf', 48)
font_shaded = pg.font.Font("font/Action_Man_Shaded.ttf", 48)
font_large_bold = pg.font.Font("font/Action_Man_Bold.ttf", 48)
font_italic = pg.font.Font("font/Action_Man_Italic.ttf", 24)
# Game Controls
game_active = False
score = 0
start_time = 0


# Running game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()





