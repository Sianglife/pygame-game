import pygame as pg
from screen.start import StartScreen
from screen.play import PlayScreen
from const.config import SCREEN_SCALE, FPS

screen = pg.display.set_mode(SCREEN_SCALE)
clock = pg.time.Clock()

current_screen = None

mode = 'start'

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    if current_screen is None:
        current_screen = StartScreen(screen)

    # elif mode == 'start':

    # current_screen.update()

    pg.display.flip()
    clock.tick(FPS)
