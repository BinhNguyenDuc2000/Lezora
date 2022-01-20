from element.element_interface import ElementInterface
import pygame as pg
from pygame import mixer

class Button(ElementInterface):

    def __init__(self, x, y, width, height, color, border_color=(255,255,255), brighten_level=0, sfx=None):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.inactive_color = color
        self.active_color = tuple(x+brighten_level if x+brighten_level < 255 else 254 for x in color)
        self.color = self.inactive_color
        self.border_color = border_color
        self.BORDER_WIDTH = 2
        self.sfx = sfx

    def draw(self, screen):
        pg.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), 0)
        pg.draw.rect(screen, self.color, (
        self.x + self.BORDER_WIDTH, self.y + self.BORDER_WIDTH, self.width - self.BORDER_WIDTH * 2,
        self.height - self.BORDER_WIDTH * 2), 0)

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.is_clicked(pos[0], pos[1]):
                if self.sfx is not None:
                    sound = mixer.Sound(self.sfx)
                    volume = mixer.music.get_volume()
                    sound.set_volume(volume if volume == 0 else volume + 0.2)
                    sound.play()
                self.color = self.active_color
            else:
                self.color = self.inactive_color

    def is_clicked(self, x, y):
        """
        if user clicked on button
        :param x: float
        :param y: float
        :return: bool
        """

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True  # user clicked button

        return False
    
    def refresh(self):
        self.color = self.inactive_color


class TextButton(Button):
    def __init__(self, x, y, width, height, text, color, font, brighten_level=0, font_color=(255, 255, 255), border_color=(255,255,255), sfx=None):
        super().__init__(x, y, width, height, color, border_color, brighten_level, sfx)
        self.text = text
        self.active_font_color = tuple(x+brighten_level for x in font_color)
        self.inactive_font_color = font_color
        self.font_color = self.inactive_font_color
        self.text_font = font

    def draw(self, screen):
        super().draw(screen)
        txt = self.text_font.render(self.text, 1, self.font_color)
        screen.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2))
    
    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.is_clicked(pos[0], pos[1]):
                self.font_color = self.active_font_color
            else:
                self.font_color = self.inactive_font_color

    def refresh(self):
        super().refresh()
        self.font_color = self.inactive_font_color
        
        
