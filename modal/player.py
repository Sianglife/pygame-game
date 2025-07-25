from modal.bullet import Bullet
import pygame as pg
import sys
from modal.object import Circle
from modal.blood import Blood


class Player(Circle):
    def __init__(self, color, radius, position=(100, 100)):
        super().__init__(color, radius, position)
        self.launch_time = 0
        self.original_image = pg.transform.scale(pg.image.load(
            'asset/player.png').convert_alpha(), (radius, radius))
        self.angle = 0
        self.bullets = pg.sprite.Group()
        self.blood = Blood(375, 255)
        self.speed = 5

    def set_speed(self, speed):
        self.speed = speed

    def kill(self):
        self.blood.kill()
        pg.quit()
        sys.exit()
        super().kill()

    def fire(self):
        bullet = Bullet((30, 10), self.rect.center,
                        self.angle, speed=self.speed+10)  # 考慮慣性，加上原本的速度
        self.bullets.add(bullet)
        self.launch_time = pg.time.get_ticks()

    def update(self):
        if self.launch_time == 0 or pg.time.get_ticks() - self.launch_time > 500:
            self.fire()

        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.blood.is_empty():
            self.kill()
