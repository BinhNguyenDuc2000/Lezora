from element.color_constant import colors
from element.button import TextButton
from element.borderless_button import BorderlessPictureButton
from screen.screen import ScreenInterface
from screen.config import DEFAULT_FONT, CLICK_SFX
import pygame as pg

class MenuScreen(ScreenInterface):
    def __init__(self):
        super().__init__()
        self.title = BorderlessPictureButton(80, 40, 480, 80, 
                                   pg.image.load("asset/sprite/Title.png"))
        self.login_button = TextButton(240, 200, 160, 60, "Login", 
                                       colors["purple"], DEFAULT_FONT, 30, font_color=colors["darkpink"], sfx=CLICK_SFX)
        self.register_button = TextButton(240, 280, 160, 60, "Register", 
                                        colors["purple"], DEFAULT_FONT, 30, font_color=colors["darkpink"], sfx=CLICK_SFX)
        



    