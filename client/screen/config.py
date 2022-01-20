import imp


import pygame as pg
from element.color_constant import colors

pg.font.init()
DEFAULT_FONT = pg.font.Font("asset/font/PixelDigivolveItalic.otf", 30)
DEFAULT_FONT_SMALL = pg.font.Font("asset/font/PixelDigivolveItalic.otf", 20)
DEFAULT_FONT_VERY_SMALL = pg.font.Font("asset/font/PixelDigivolveItalic.otf", 10)
DEFAULT_SCREEN_COLOR = colors["darkblue"]
DEFAULT_SCREEN_WIDTH = 640
DEFAULT_SCREEN_HEIGHT = 400

MAX_VOLUME = 0.1
MIN_VOLUME = 0.0

CLICK_SFX = "asset/sfx/Menu_Click_Single_Medium_01.wav"

CARD_TIRED = "asset/sprite/cardtired.png"
CARD_SWORD = "asset/sprite/cardsword.png"
CARD_GUN = "asset/sprite/cardgun.png"
CARD_SHIELD  = "asset/sprite/cardshield.png"

CARD_UNKNOWN = "asset/sprite/cardunknown.png"

cards = dict()
cards["-1"] = pg.image.load(CARD_UNKNOWN)
cards["0"] = pg.image.load(CARD_TIRED)
cards["1"] = pg.image.load(CARD_SWORD)
cards["2"] = pg.image.load(CARD_GUN)
cards["3"] = pg.image.load(CARD_SHIELD)