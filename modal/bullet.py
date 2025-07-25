import math
import pygame as pg
from enum import Enum
from modal.object import GameObject
from modal.player import player
from modal.enemy import enemies

image = ['asset/bullet.png', 'asset/bullet-npc.png']


class BulletRole(Enum):
    PLAYER = 0
    ENEMY = 1


class Bullet(GameObject):
    def __init__(self, size, position=(100, 100), angle=0, role=BulletRole.PLAYER, start_speed=0):
        super().__init__(size, position)
        self.original_image = pg.transform.scale(pg.image.load(
            image[role.value]).convert_alpha(), size)
        self.angle = angle
        self.move_speed = start_speed + 10
        self.set_angle(angle)
        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=position)

    def update(self):
        # move bullet
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

        # check if bullet hit player or enemy
        if self.role == BulletRole.PLAYER:
            collided_enemies = pg.sprite.spritecollideany(
                self, enemies, dokill=True)
            if collided_enemies:
                collided_enemies.blood.damage(50)
                self.kill()
        elif self.role == BulletRole.ENEMY:
            if pg.sprite.collide_rect(self, player):
                player.blood.damage(10)
                self.kill()

        super().update()

    def set_angle(self, angle):
        self.angle = angle
        rad = math.radians(angle)
        self.delta_x = self.move_speed * math.cos(rad)
        self.delta_y = -self.move_speed * math.sin(rad)
        self.image = pg.transform.rotate(self.original_image, angle)
