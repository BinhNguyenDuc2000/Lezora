from element.color_constant import colors
from element.button import TextButton
from screen.screen import ScreenInterface
from screen.config import DEFAULT_FONT, CLICK_SFX

class LoadingScreen(ScreenInterface):
    def __init__(self, text="Loading"):
        super().__init__()
        self.error_message = TextButton(120, 80, 400, 100, text, colors["purple"], DEFAULT_FONT, 0, 
                                        border_color=colors["darkpink"],
                                        font_color=colors["darkpink"])