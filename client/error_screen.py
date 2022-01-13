import pygame as pg
from color_constant import colors
from network import Network
from button import TextButton
from input_box import InputBox
from screen import ScreenInterface

class ErrorScreen(ScreenInterface):
    def __init__(self, message):
        self.error_message = TextButton(150, 80, 340, 100, message, active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])

        self.try_again_button = TextButton(250, 240, 140, 40, "Try again", colors["gray"])
