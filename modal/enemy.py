from modal.bullet import Bullet
import pygame as pg
from modal.object import GameObject
from const.config import SCREEN_SCALE
from modal.blood import Blood
import random


class Enemy(GameObject):
    def __init__(self, radius, position=(100, 100), die_handler=None):
        super().__init__((radius, radius), position)
        self.ori_image = pg.transform.scale(pg.image.load(
            'asset/enemies.png').convert_alpha(), (radius, radius))
        self.image = self.ori_image
        self.rect = self.ori_image.get_rect(center=position)
        self.rect.topleft = position
        self.angle = random.choice([0, 90, 180, 270])
        self.speed = 2
        self.bullets = pg.sprite.Group()
        self.blood = Blood(self.rect.x, self.rect.y - 15)
        self.launch_time = 0
        self.die_handler = die_handler

    def fire(self):
        bullet = Bullet((30, 10), self.rect.center, self.angle,
                        role=1, speed=self.speed+10)
        self.bullets.add(bullet)
        self.launch_time = pg.time.get_ticks()

    def update(self):

        if self.angle == 0:
            self.rect.x += self.speed
        elif self.angle == 90:
            self.rect.y -= self.speed
        elif self.angle == 180:
            self.rect.x -= self.speed
        elif self.angle == 270:
            self.rect.y += self.speed

        if self.blood.is_empty():
            if self.die_handler:
                self.die_handler()
            self.kill()

        # +-300才能追出去的感覺
        if self.rect.x < -300 or self.rect.x > SCREEN_SCALE[0]+300 or self.rect.y < -300 or self.rect.y > SCREEN_SCALE[1]+300:
            self.kill()

        # if self.launch_time == 0 or pg.time.get_ticks() - self.launch_time > 500:
        #     self.fire()

        self.rect = self.ori_image.get_rect(center=self.rect.center)
        self.blood.goto(self.rect.x, self.rect.y - 15)
        self.image = pg.transform.rotate(self.ori_image, self.angle)
