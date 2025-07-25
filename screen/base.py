import pygame as pg
from pygame_gui import UIManager
from const.config import SCREEN_SCALE, FPS


class Screen:
    gmgr = UIManager(SCREEN_SCALE)

    def __init__(self, screen, clock, bg_color=(0, 0, 0), exit=None):
        self.screen = screen
        self.clock = clock
        self.background_color = bg_color
        self.backgroundObjects = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.exit = exit

    def update(self):
        self.all_sprites.add(*self.backgroundObjects)
        self.all_sprites.update()
        self.e = pg.event.wait()
        self.gmgr.process_events(self.e)
        self.gmgr.update(self.clock.tick(FPS) / 1000.0)
        self.draw()

    def draw(self):
        self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)
        self.gmgr.draw_ui(self.screen)

    def end(self):
        self.gmgr.clear_and_reset()
        self.backgroundObjects.empty()
        self.all_sprites.empty()
        if self.exit:
            self.exit()

    def move_bg(self, dx, dy, reverse=True, check_collision=None):
        if reverse:
            dx = -dx
            dy = -dy

        for sprite in self.all_sprites:
            sprite.rect.x += dx
            sprite.rect.y += dy

        if check_collision and check_collision():
            self.move_bg(-dx, -dy, reverse=False)

