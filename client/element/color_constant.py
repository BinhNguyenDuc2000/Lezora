"""Provide RGB color constants and a colors dictionary with
elements formatted: colors[colorname] = CONSTANT"""
from collections import namedtuple
Color = namedtuple('RGB', 'red, green, blue')
colors = {}  # dict of colors

class RGB(Color):
    def hex_format(self):
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)
# Color Contants
BLUE = RGB(121, 152, 238)
DARKBLUE = RGB(12, 30, 127)
PURLE = RGB(97, 40, 151)
DARKPURPLE = RGB(70, 30, 82)
PINK = RGB(215, 123, 186)
DARKPINK = RGB(210, 29, 121)
WHITE = RGB(255, 255, 255)
BLACK = RGB(0, 0 ,0)
SILVER = RGB(192, 192, 192)
DARKSILVER = RGB(119, 136, 153)
ORANGE = RGB(230, 142, 54)


colors["blue"] = BLUE
colors["darkblue"] = DARKBLUE
colors["purple"] = PURLE
colors["darkpurple"] = DARKPURPLE
colors["pink"] = PINK
colors["darkpink"] = DARKPINK
colors["white"] = WHITE
colors["black"] = BLACK
colors["silver"] = SILVER
colors["darksilver"] = DARKSILVER
colors["orange"] = ORANGE