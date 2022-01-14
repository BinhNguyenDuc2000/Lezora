from element.color_constant import colors
from element.button import TextButton
from element.input_box import InputBox
from screen.screen import ScreenInterface

class LoginScreen(ScreenInterface):
    def __init__(self):
        self.back_button = TextButton(0, 0, 80, 40, "Back", colors["gray"])
        self.login_label = TextButton(220, 10, 200, 60, "Login", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.username_label = TextButton(160, 80, 160, 40, "Username", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.username_box = InputBox(160, 130, 320, 40)
        self.password_label = TextButton(160, 210, 160, 40, "Password", active_color = colors["purple4"],
            border_color=colors["deeppink1"], inactive_color=colors["purple4"], font_color=colors["deeppink1"])
        self.password_box = InputBox(160, 260, 320, 40)
        self.submit_button = TextButton(260, 320, 120, 40, "Submit", colors["gray"])
        