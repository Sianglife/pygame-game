import random
import pygame as pg
from modal.bullet import Bullet
from modal.object import GameObject
from modal.blood import Blood
from modal.obstacles import obstacles
from modal.player import player
from const.event import ENEMY_DIE, CHECK_DAMAGE

enemies = pg.sprite.Group()


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
        # move enemy
        if self.angle == 0:
            self.rect.x += self.speed
        elif self.angle == 90:
            self.rect.y -= self.speed
        elif self.angle == 180:
            self.rect.x -= self.speed
        elif self.angle == 270:
            self.rect.y += self.speed

        # check collision with player and other enemies
        for e in pg.event.get():
            if e.type == CHECK_DAMAGE:
                collided = pg.sprite.spritecollide(self, obstacles, False)
                if collided:
                    self.blood.damage(10)
                    self.angle = (self.angle + 180) % 360

                collided = pg.sprite.spritecollide(self, player, False)
                if collided:
                    player.blood.damage(10)
                    self.blood.damage(10)
                    self.angle = (self.angle + 180) % 360

                collided = pg.sprite.spritecollide(self, enemies, False)
                if collided:
                    for enemy in collided:
                        if enemy != self:
                            enemy.blood.damage(10)
                            self.angle = (self.angle + 180) % 360

        # check if died
        if self.blood.is_empty():
            pg.event.post(pg.event.Event(ENEMY_DIE, {'enemy': self}))
            enemies.remove(self)
            self.kill()

        self.rect = self.ori_image.get_rect(center=self.rect.center)
        self.blood.goto(self.rect.x, self.rect.y - 15)
        self.image = pg.transform.rotate(self.ori_image, self.angle)
        super().update()
