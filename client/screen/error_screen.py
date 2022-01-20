from element.color_constant import colors
from element.button import TextButton
from screen.screen import ScreenInterface

class ErrorScreen(ScreenInterface):
    def __init__(self, message):
        self.error_message = TextButton(150, 80, 340, 100, message, active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])

        self.try_again_button = TextButton(250, 240, 140, 40, "Try again", colors["gray"])
        
class LoginErrorScreen(ErrorScreen):
    error_dict = {}
    error_dict["PLAYERNOTFOUND"] = "Player is not found"
    error_dict["PLAYERALREADYONLINE"] = "Player is already online"
    error_dict["INVALIDINPUT"] = "Invalid input"
    def __init__(self, message):
        super().__init__(LoginErrorScreen.error_dict[message])
        
class RegisterErrorScreen(ErrorScreen):
    error_dict = {}
    error_dict["PLAYERALREADYEXCIST"] = "Player already excist"
    def __init__(self, message):
        super().__init__(RegisterErrorScreen.error_dict[message])
