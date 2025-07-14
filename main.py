import pygame as pg
import sys
from const.color import *
from modal.object import Rectangle
from modal.player import Player
from modal.enemies import Enemies


SCREEN_SCALE = (800, 600)
FPS = 60

pg.init()
pg.display.set_caption("window Game")

screen = pg.display.set_mode(SCREEN_SCALE)
clock = pg.time.Clock()


# 物件初始化
player = Player(WHITE, 50, (400, 300))

obstacles = pg.sprite.Group(
    Rectangle(BLUE, (200, 150), (100, 100)),
    Rectangle(GREEN, (100, 100), (200, 400))
)

enemies = pg.sprite.Group(
    Enemies(RED, 50, (200, 200)),
    Enemies(RED, 50, (600, 400))
)
# *代表解包，把obstacles每一項物件都加入到all_sprites中
backgroundObjects = pg.sprite.Group(*obstacles)


def check_collision():
    if pg.sprite.spritecollide(player, obstacles, False):
        return True
    return False


def move_background(dx, dy, reverse=True, recursive=True):
    # 反向移動
    if reverse:
        dx = -dx
        dy = -dy

    for sprite in backgroundObjects:
        sprite.move(dx, dy)

    if recursive and check_collision():
        move_background(-dx, -dy, reverse=False,
                        recursive=False)  # 如果碰到障礙物就退一步


# 主迴圈
while True:
    # Player update
    player.update()

    # move bullet
    for bullet in player.bullets:
        bullet.update()
        if bullet.rect.x < 0 or bullet.rect.x > SCREEN_SCALE[0] or bullet.rect.y < 0 or bullet.rect.y > SCREEN_SCALE[1]:
            player.bullets.remove(bullet)
            all_sprites.remove(bullet)

    # Update draw
    screen.fill(BLACK)
    backgroundObjects = pg.sprite.Group(*obstacles, *enemies)
    all_sprites = pg.sprite.Group(
        player, *obstacles, *enemies, *player.bullets, player.blood)
    all_sprites.draw(screen)
    pg.display.flip()

    # Check keyboard input
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and keys[pg.K_DOWN]:
        move_background(-5, 5)
        player.angle = 225
    elif keys[pg.K_LEFT] and keys[pg.K_UP]:
        move_background(-5, -5)
        player.angle = 135
    elif keys[pg.K_RIGHT] and keys[pg.K_DOWN]:
        move_background(5, 5)
        player.angle = 315
    elif keys[pg.K_RIGHT] and keys[pg.K_UP]:
        move_background(5, -5)
        player.angle = 45
    elif keys[pg.K_LEFT]:
        move_background(-5, 0)
        player.angle = 180
    elif keys[pg.K_RIGHT]:
        move_background(5, 0)
        player.angle = 0
    elif keys[pg.K_UP]:
        move_background(0, -5)
        player.angle = 90
    elif keys[pg.K_DOWN]:
        move_background(0, 5)
        player.angle = 270
    if keys[pg.K_r]:
        player.reset()
        for obstacle in obstacles:
            obstacle.reset()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()

    clock.tick(FPS)
