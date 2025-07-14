
import const.color as color
import pygame as pg
from modal.object import Rectangle


class Blood(Rectangle):
    def __init__(self, x, y):
        super().__init__(color.BLACK, (200, 20), (x, y))
        self.hp = 100
        self.blood = pg.Surface((200, 20))
        self.blood.fill(color.RED)
        self.blood_rect = self.blood.get_rect(topleft=(x, y))

    def update(self):
        blood_width = int(self.hp / 100 * 200)
        blood_surface = pg.Surface((blood_width, 20))
        blood_surface.fill(color.RED)
        blood_rect = blood_surface.get_rect(topleft=(self.blood_rect.topleft))
        self.blood = blood_surface
        self.blood_rect = blood_rect
        
    def damage(self, value):
        self.hp -= value
        if self.hp < 0:
            self.hp = 0
        self.update()

