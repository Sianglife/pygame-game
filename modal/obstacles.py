import pygame as pg
from modal.object import Rectangle
import const.color as color

obstacles = pg.sprite.Group(
    Rectangle(color.BLUE, (200, 150), (100, 100)),
    Rectangle(color.GREEN, (100, 100), (200, 400))
)
