
import const.color as color
import pygame as pg
from modal.object import Rectangle


class Blood(Rectangle):
    def __init__(self, x, y):
        super().__init__(color.RED, (50, 10), (x, y))
        self.hp = 100

    def update(self):
        blood_width = max(0, int(self.hp / 100 * 50))

        self.image = pg.Surface((50, 10))
        self.image.fill(pg.Color("black"))

        # 畫上血量部分
        if blood_width > 0:
            red_bar = pg.Surface((blood_width, 10))
            red_bar.fill(color.RED)
            self.image.blit(red_bar, (0, 0))

        self.rect = self.image.get_rect(topleft=self.rect.topleft)

        super().update()

    def goto(self, x, y):
        self.rect.topleft = (x, y)

    def damage(self, value):
        self.hp -= value
        if self.hp < 0:
            self.hp = 0
        self.update()

    def is_empty(self):
        return self.hp <= 0
