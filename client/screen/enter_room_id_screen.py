from element.color_constant import colors
from element.button import TextButton
from element.input_box import InputBox
from screen.screen import ScreenInterface
from screen.config import CLICK_SFX, DEFAULT_FONT

class EnterRoomIDScreen(ScreenInterface):
    def __init__(self):
        super().__init__()
        self.back_button = TextButton(0, 0, 100, 40, "Back", colors["purple"], 
                                      DEFAULT_FONT, brighten_level=10, font_color=colors["darkpink"], sfx=CLICK_SFX)
        self.login_label = TextButton(220, 10, 240, 60, "Enter room ID", color = colors["purple"], font = DEFAULT_FONT,
            border_color=colors["darkpink"], font_color=colors["darkpink"])
        self.room_id_label = TextButton(160, 80, 200, 40, "RoomID", color = colors["purple"], font = DEFAULT_FONT,
            border_color=colors["darkpink"], font_color=colors["darkpink"])
        self.room_id_box = InputBox(160, 130, 320, 40, colors["darkpink"], DEFAULT_FONT, brigten_level=30, sfx=CLICK_SFX)
        self.submit_button = TextButton(260, 290, 120, 40, "Submit", colors["darksilver"], 
                                      DEFAULT_FONT, brighten_level=10, font_color=colors["silver"], sfx=CLICK_SFX)