import pygame as pg
from random import randint, choice

import pygame.event

# CONSTANTS
WIDTH = 800
HEIGHT = 600
FPS = 60


class Student(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('graphics/student/Student2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WIDTH / 2, HEIGHT - 10))

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

    def update(self):
        self.move()




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

# Screen Background
bg_surface = pg.image.load('graphics/BACKGROUND.png').convert()

# student
student = pg.sprite.GroupSingle()
student.add(Student())


# Running game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # Adding background to the game
    screen.blit(bg_surface, (0, 0))

    # Adding player to the game
    student.draw(screen)
    student.update()


    # updating display
    pg.display.update()
    # maintaining fps
    clock.tick(FPS)


