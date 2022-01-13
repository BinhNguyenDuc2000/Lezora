import pygame as pg
from color_constant import colors
from network import Network
from button import TextButton
from input_box import InputBox
from screen import ScreenInterface

class RegisterScreen(ScreenInterface):
    def __init__(self):
        self.back_button = TextButton(0, 0, 60, 40, "Back", colors["gray"])
        self.login_label = TextButton(220, 10, 200, 60, "Register", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.username_label = TextButton(160, 80, 160, 40, "Username", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.username_box = InputBox(160, 130, 320, 40)
        self.password_label = TextButton(160, 210, 160, 40, "Password", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.password_box = InputBox(160, 260, 320, 40)
        self.submit = TextButton(260, 320, 120, 40, "Submit", colors["gray"])