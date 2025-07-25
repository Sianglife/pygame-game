from modal.object import GameObject
import pygame as pg
import math

image = ['asset/bullet.png', 'asset/bullet-npc.png']


class Bullet(GameObject):
    def __init__(self, size, position=(100, 100), angle=0, role=0, speed=10):
        super().__init__(size, position)
        self.original_image = pg.transform.scale(pg.image.load(
            image[role]).convert_alpha(), size)
        self.angle = angle  # 子彈的角度
        self.move_speed = speed  # 子彈移動速度
        self.set_angle(angle)  # 設定角度與移動向量
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

    def set_angle(self, angle):
        self.angle = angle
        rad = math.radians(angle)
        self.delta_x = self.move_speed * math.cos(rad)
        self.delta_y = -self.move_speed * math.sin(rad)
        self.image = pg.transform.rotate(self.original_image, angle)
