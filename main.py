import random

import pygame

FPS = 30
WIDTH = 1920
HEIGHT = 1080
COL_SIZE = 15
ROW_SIZE = 15
COLS_NUM = int(WIDTH / COL_SIZE)
KATAKANA_FONT_SIZE = 23
KATAKANA_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijkl!<"
SECOND_FONT_SIZE = 20
SECOND_CHARS = "0123456789!<>=+-"

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
katakana_font = pygame.font.Font("katakana.ttf", KATAKANA_FONT_SIZE)
second_font = pygame.font.SysFont(None, SECOND_FONT_SIZE)
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
        letter = katakana_font.render(random.choice(list(KATAKANA_CHARS)), True, c)
        if random.random() < 0.1:
            letter = second_font.render(random.choice(list(SECOND_CHARS)), True, c)
        letter = pygame.transform.flip(letter, True, False)
        screen.blit(letter, (i * COL_SIZE, column * ROW_SIZE))
        columns[i] += 1
        if columns[i] > 30 + random.random() * 2000:
            columns[i] = 0
    s = pygame.Surface((WIDTH, HEIGHT))
    s.set_alpha(7)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))
    pygame.display.update()
    # scaled = pygame.transform.smoothscale(screen, (WIDTH + 1, HEIGHT + 1))
    # screen.blit(scaled, (-1, -1))
