from modal.bullet import Bullet
import pygame as pg
from modal.object import GameObject
from const.config import SCREEN_SCALE
from modal.blood import Blood, blood


class Enemy(GameObject):
    def __init__(self, radius, position=(100, 100)):
        super().__init__((radius, radius), position)
        self.image = pg.transform.scale(pg.image.load(
            'asset/enemies.png').convert_alpha(), (radius, radius))
        self.rect = self.image.get_rect(center=position)
        self.rect.topleft = position
        self.angle = 0  # random.choice([0, 90, 180, 270])
        self.speed = 2
        # self.bullets = pg.sprite.Group()
        self.blood = Blood(self.rect.x, self.rect.y - 15)
        blood.add(self.blood)

    # def fire(self):
        # bullet = Bullet((30, 10), self.rect.center, self.angle, role=1)
        # self.bullets.add(bullet)
        # self.launch_time = pg.time.get_ticks()

    def update(self):
        self.blood.goto(self.rect.x, self.rect.y - 15)
        if self.angle == 0:
            self.rect.x += self.speed
        elif self.angle == 90:
            self.rect.y -= self.speed
        elif self.angle == 180:
            self.rect.x -= self.speed
        elif self.angle == 270:
            self.rect.y += self.speed

        self.image = pg.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.blood.is_empty():
            self.blood.kill()
            blood.remove(self.blood)
            self.kill()

        if self.rect.x < 0 or self.rect.x > SCREEN_SCALE[0] or self.rect.y < 0 or self.rect.y > SCREEN_SCALE[1]:
            self.blood.kill()
            blood.remove(self.blood)
            self.kill()
