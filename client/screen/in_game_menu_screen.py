import pygame as pg
from screen.screen import ScreenInterface
from screen.config import DEFAULT_FONT_SMALL, CLICK_SFX
from element.color_constant import colors
from element.button import TextButton

class InGameMenuScreen(ScreenInterface):
    def __init__(self, username, rank):
        super().__init__()
        username_text = "Hello, " + username
        self.username_text = TextButton(70, 20, 500, 60, username_text, colors["purple"], font=DEFAULT_FONT_SMALL, 
            border_color=colors["darkpink"], font_color=colors["darkpink"])
        
        rank_text = "Your rank is " + str(rank)
        self.rank_text = TextButton(70, 90, 500, 60, rank_text, colors["purple"], font=DEFAULT_FONT_SMALL, 
            border_color=colors["darkpink"], font_color=colors["darkpink"])
        
        self.create_room_button = TextButton(170, 170, 300, 40, "Create Room", 
            colors["purple"], DEFAULT_FONT_SMALL, 30, font_color=colors["darkpink"], sfx=CLICK_SFX)
        self.join_room_button = TextButton(170, 230, 300, 40, "Join Room", 
            colors["purple"], DEFAULT_FONT_SMALL, 30, font_color=colors["darkpink"], sfx=CLICK_SFX)
        self.logout_button = TextButton(170, 290, 300, 40, "Log out", 
            colors["purple"], DEFAULT_FONT_SMALL, 30, font_color=colors["darkpink"], sfx=CLICK_SFX)