import pygame as pg
from color_constant import colors
from network import Network
from button import TextButton
from screen import ScreenInterface

class MenuScreen(ScreenInterface):
    def __init__(self):
        self.logo = TextButton(160, 40, 320, 60, "Lezora", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.logo.change_font_size(50)
        self.login_button = TextButton(240, 200, 160, 60, "Login", colors["gray"])
        self.register_button = TextButton(240, 280, 160, 60, "Register", colors["gray"])


    