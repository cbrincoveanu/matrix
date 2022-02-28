import random

import pygame

FPS = 30
FONT_SIZE = 25
COLS_NUM = 130
COL_SIZE = 15
ROW_SIZE = 15
WIDTH = 1920
HEIGHT = 1080
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijkl!<"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
font = pygame.font.Font("katakana.ttf", 20)  # pygame.font.SysFont(None, FONT_SIZE)
clock = pygame.time.Clock()

columns = [0 for _ in range(COLS_NUM)]
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    for i, column in enumerate(columns):
        c = (0, 120 + random.randint(0, 120), 0)
        if random.random() < 0.01:
            c = (255, 255, 255)
        letter = font.render(random.choice(list(CHARS)), True, c)
        letter = pygame.transform.flip(letter, True, False)
        screen.blit(letter,
                    (i * COL_SIZE, column * ROW_SIZE))
        columns[i] += 1
        if columns[i] > 30 + random.random() * 2000:
            columns[i] = 0
    s = pygame.Surface((WIDTH, HEIGHT))
    s.set_alpha(3)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    pygame.display.update()
