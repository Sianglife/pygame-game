from modal.bullet import Bullet
import pygame as pg
from modal.object import Circle
from modal.blood import Blood
import random


class Enemies(Circle):
    def __init__(self, color, radius, position=(100, 100)):
        super().__init__(color, radius, position)
        self.launch_time = 0
        self.original_image = pg.transform.scale(pg.image.load(
            'asset/enemies.png').convert_alpha(), (radius, radius))
        # Only four directions: 0, 90, 180, 270
        self.angle = random.choice([0, 90, 180, 270])
        self.bullets = pg.sprite.Group()
        self.blood = Blood(375, 250)
        self.move_time = pg.time.get_ticks()
        self.move_interval = 1000  # ms
        self.speed = 5
        self.update()

    def fire(self):
        bullet = Bullet((30, 10), self.rect.center, self.angle, role=1)
        self.bullets.add(bullet)
        self.launch_time = pg.time.get_ticks()

    def move(self, dx=0, dy=0):
        # Move only in four directions
        if self.angle == 0:      # Right
            self.rect.x -= self.speed + dx
            self.rect.y -= dy
        elif self.angle == 90:   # Up
            self.rect.y += self.speed - dy
            self.rect.x -= dx
        elif self.angle == 180:  # Left
            self.rect.x += self.speed - dx
            self.rect.y -= dy
        elif self.angle == 270:  # Down
            self.rect.y -= self.speed + dy
            self.rect.x -= dx
        # Move only in four directions
        if self.angle == 0:      # Right
            self.rect.x -= self.speed
        elif self.angle == 90:   # Up
            self.rect.y -= self.speed
        elif self.angle == 180:  # Left
            self.rect.x += self.speed
        elif self.angle == 270:  # Down
            self.rect.y += self.speed

    def update(self, move_bg_offset=(0, 0)):
        # Randomly change angle every move_interval ms
        now = pg.time.get_ticks()
        if now - self.move_time > self.move_interval:
            self.angle = random.choice([0, 90, 180, 270])
            self.move_time = now

        # self.move()

        # Move with background offset from main.py
        self.rect.x += move_bg_offset[0]
        self.rect.y += move_bg_offset[1]

        if self.launch_time == 0 or now - self.launch_time > 500:
            self.fire()
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.blood.update()
