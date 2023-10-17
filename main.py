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


class SolutionArrow(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('graphics/student/Solution_bullet_2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WIDTH/2,  HEIGHT + 80))
        self.active = False

    def reset(self):
        if self.rect.bottom < 0:
            self.active = False
            self.rect.midbottom = (WIDTH/2, HEIGHT + 80)

    def start_movement(self, x_pos):
        pg.key.get_pressed()
        if pg.key.get_pressed()[pg.K_SPACE] and not self.active:
            self.rect.midbottom = (x_pos - 20, HEIGHT - 70)
            self.active = True

    def update(self, x_pos):
        self.start_movement(x_pos)
        if self.active: self.rect.y -= 5
        self.reset()


class Assignments(pg.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        self.image = pg.image.load('graphics/assignment/Assignment_scroll.png').convert_alpha()
        self.image = pg.transform.rotozoom(self.image, 0, 0.5)
        self.x_pos = [WIDTH // 2 - i * 70 for i in [0, -1, 1, -2, 2, 3, -3]]
        self.rect = self.image.get_rect(midtop=(self.x_pos[number], 80))
        self.initial_x_pos = self.x_pos[number]
        self.move_by_pixels = 2

    def move(self):
        if abs(self.rect.x - self.initial_x_pos) >= 200:
            self.move_by_pixels *= -1
        self.rect.x += self.move_by_pixels
        # print(self.rect.x, self.initial_x_pos, self.move_by_pixels)

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
game_active = True
score = 0
start_time = 0

# Screen Background
bg_surface = pg.image.load('graphics/BACKGROUND.png').convert()

# student
student = pg.sprite.GroupSingle(Student())

# solution arrow
solution_arrow = pg.sprite.GroupSingle(SolutionArrow())

# Assignments Group
assignments = pg.sprite.Group([Assignments(i) for i in range(7)])
# Running game loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    if game_active:
        # Adding background to the game
        screen.blit(bg_surface, (0, 0))

        # Adding player to the game
        student.draw(screen)
        student.update()

        # Adding Assignments to the game
        assignments.draw(screen)
        assignments.update()

        # Adding solution arrow to the game
        solution_arrow.draw(screen)
        solution_arrow.update(student.sprite.rect.centerx)

    # updating display
    pg.display.update()
    # maintaining fps
    clock.tick(FPS)


