import pygame as pg
from const.config import SCREEN_SCALE, BOARD_BUFFER


class GameObject(pg.sprite.Sprite):
    def __init__(self, size, position=(100, 100)):
        super().__init__()
        self.ori_size = size  # 儲存原始大小
        self.ori_position = position  # 儲存原始位置

    def move(self, dx, dy):
        # 移動物件
        self.rect.x += dx
        self.rect.y += dy

    def set_position(self, position):
        # 設定位置
        self.rect.topleft = position

    def reset(self):
        # 重置大小和位置
        self.rect.topleft = self.ori_position
        self.rect.size = self.ori_size

    def update(self):
        """
        Check if the object is out of bounds.
        """
        if (self.rect.x < -BOARD_BUFFER or self.rect.x > SCREEN_SCALE[0] + BOARD_BUFFER or
                self.rect.y < -BOARD_BUFFER or self.rect.y > SCREEN_SCALE[1] + BOARD_BUFFER):
            self.kill()


class Circle(GameObject):
    def __init__(self, color, circle_radius, position=(100, 100)):
        super().__init__((circle_radius * 2, circle_radius * 2), position)
        self.image = pg.Surface(
            (circle_radius * 2, circle_radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.image, color, (circle_radius,
                       circle_radius), circle_radius)
        self.rect = self.image.get_rect(center=position)

    def update(self):
        return super().update()


class Rectangle(GameObject):
    def __init__(self, color, size, position=(100, 100)):
        super().__init__(size, position)
        self.ori_position = position
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=position)

    def update(self):
        return super().update()
