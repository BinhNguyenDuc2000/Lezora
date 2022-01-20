from element.color_constant import colors
from element.button import TextButton
from screen.screen import ScreenInterface
from screen.config import DEFAULT_FONT, CLICK_SFX

class ErrorScreen(ScreenInterface):
    def __init__(self, message):
        super().__init__()
        self.error_message = TextButton(20, 80, 600, 100, message, colors["purple"], font=DEFAULT_FONT, 
            border_color=colors["darkpink"], font_color=colors["darkpink"])

        self.try_again_button = TextButton(220, 240, 200, 40, "Try again", colors["darksilver"], 
                                           font=DEFAULT_FONT, brighten_level=30, font_color=colors["silver"],
                                           sfx=CLICK_SFX)
        
class LoginErrorScreen(ErrorScreen):
    error_dict = {}
    error_dict["PLAYERNOTFOUND"] = "Player is not found"
    error_dict["PLAYERALREADYONLINE"] = "Player is already online"
    error_dict["INVALIDINPUT"] = "Invalid input"
    def __init__(self, message):
        super().__init__(LoginErrorScreen.error_dict[message])
        
class RegisterErrorScreen(ErrorScreen):
    error_dict = {}
    error_dict["PLAYERALREADYEXIST"] = "Player already exist"
    def __init__(self, message):
        super().__init__(RegisterErrorScreen.error_dict[message])
        
class InGameMenuErrorScreen(ErrorScreen):
    error_dict = {}
    error_dict["INVALIDGAME"] = "Game ID is invalid"
    def __init__(self, message):
        super().__init__(InGameMenuErrorScreen.error_dict[message])
