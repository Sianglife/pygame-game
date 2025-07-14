from modal.bullet import Bullet
import pygame as pg
from modal.object import Circle
from modal.blood import Blood
from modal.bullet import bullets
import math


class Player(Circle):
    def __init__(self, color, radius, position=(100, 100)):
        super().__init__(color, radius, position)
        self.launch_time = 0  # 記錄發射子彈的時間
        self.original_image = pg.transform.scale(pg.image.load(
            'asset/player.png').convert_alpha(), (radius, radius))
        self.angle = 0
        self.blood = Blood(100, 100)
        self.update()

    def fire(self):
        if self.launch_time and pg.time.get_ticks() - self.launch_time < 500:
            return

        bullet = Bullet((30, 10), self.rect.center, self.angle)
        bullets.add(bullet)
        self.launch_time = pg.time.get_ticks()

    def update(self):
        # set angle with mouse position
        mouse_x, mouse_y = pg.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx))
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.blood.update()
