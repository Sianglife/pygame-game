from screen.base import Screen
from pygame_gui.elements import UIButton
from modal.score import Score
import pygame_gui as gui
import pygame as pg
from const.config import SCREEN_SCALE


class StartScreen(Screen):
    def __init__(self, screen, exit=None):
        super().__init__(screen, exit=exit)
        self.init_gui()

    def init_gui(self):
        self.btn_start = UIButton(
            relative_rect=pg.Rect(
                ((SCREEN_SCALE[0]/2)-50, (SCREEN_SCALE[1]/2)-25), (100, 50)),
            text='Start',
            manager=self.gmgr
        )

    def update(self):
        e = pg.event.wait()
        if e.type == gui.UI_BUTTON_PRESSED:
            if e.ui_element == self.btn_start:
                self.btn_start.hide()
        super().update()
