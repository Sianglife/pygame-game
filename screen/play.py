import random
import pygame as pg
from screen.base import Screen
from modal.score import Score
from modal.enemy import enemies, Enemy
from modal.player import player
from modal.obstacles import obstacles
from const.event import ENEMY_SPAWN_EVENT, CHECK_DAMAGE, ENEMY_DIE


class PlayScreen(Screen):
    def __init__(self, screen, exit=None):
        super().__init__(screen, exit=exit)
        self.init_gui()
        self.backgroundObjects.add(*obstacles)
        self.all_sprites.add(player, *obstacles, player.blood)
        pg.time.set_timer(ENEMY_SPAWN_EVENT, 3000)

    def init_gui(self):
        self.score = Score()

    def check_collision(self):
        if pg.sprite.spritecollide(player, obstacles, False):
            return True
        return False

    def update(self):
        # Add custom objects to all_sprites
        enemies_objs = pg.sprite.Group()
        for enemy in enemies:
            enemies_objs.add(*enemy.bullets, enemy.blood)
        self.backgroundObjects.add(*enemies, *enemies_objs)
        self.all_sprites.add(*player.bullets, *self.backgroundObjects)

        # Check keyboard input
        keys = pg.key.get_pressed()
        speed = player.speed
        if keys[pg.K_LEFT] and keys[pg.K_DOWN]:
            self.move_bg(-speed, speed)
            player.angle = 225
        elif keys[pg.K_LEFT] and keys[pg.K_UP]:
            self.move_bg(-speed, -speed)
            player.angle = 135
        elif keys[pg.K_RIGHT] and keys[pg.K_DOWN]:
            self.move_bg(speed, speed)
            player.angle = 315
        elif keys[pg.K_RIGHT] and keys[pg.K_UP]:
            self.move_bg(speed, -speed)
            player.angle = 45
        elif keys[pg.K_LEFT]:
            self.move_bg(-speed, 0)
            player.angle = 180
        elif keys[pg.K_RIGHT]:
            self.move_bg(speed, 0)
            player.angle = 0
        elif keys[pg.K_UP]:
            self.move_bg(0, -speed)
            player.angle = 90
        elif keys[pg.K_DOWN]:
            self.move_bg(0, speed)
            player.angle = 270
        if keys[pg.K_r]:
            player.reset()
            for obstacle in obstacles:
                obstacle.reset()

        for e in pg.event.get():
            if e.type == ENEMY_DIE:
                self.score.plus()
                
            if e.type == ENEMY_SPAWN_EVENT:
                enemy = Enemy(50, (random.randint(100, 400),
                                   random.randint(100, 400)))
                if pg.sprite.spritecollideany(enemy, obstacles) or pg.sprite.spritecollideany(enemy, enemies) or pg.sprite.collide_rect(enemy, player):
                    while pg.sprite.spritecollideany(enemy, obstacles) or pg.sprite.spritecollideany(enemy, enemies) or pg.sprite.collide_rect(enemy, player):
                        enemy.rect.x = random.randint(100, 400)
                        enemy.rect.y = random.randint(100, 400)
                enemies.add(enemy)
