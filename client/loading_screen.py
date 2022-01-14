from color_constant import colors
from button import TextButton
from screen import ScreenInterface

class LoadingScreen(ScreenInterface):
    def __init__(self):
        self.error_message = TextButton(150, 80, 340, 100, "Loading", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])