import pygame as pg
from pygame import mixer
from element.element_interface import ElementInterface

class BorderlessButton(ElementInterface):

    def __init__(self, x, y, width, height, sfx=None):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.BORDER_WIDTH = 2
        self.sfx = sfx
    
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
    
    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.is_clicked(pos[0], pos[1]):
                if self.sfx is not None:
                    sound = mixer.Sound(self.sfx)
                    volume = mixer.music.get_volume()
                    sound.set_volume(volume if volume == 0 else volume + 0.2)
                    sound.play()

class BorderlessPictureButton(BorderlessButton):
    def __init__(self, x, y, width, height, image, brighten_level = 0, sfx=None):
        super().__init__(x, y, width, height, sfx=sfx)
        self.active_image = image
        self.inactive_image = image.copy()
        self.active_image.fill((brighten_level, brighten_level, brighten_level), special_flags=pg.BLEND_RGB_ADD)
        self.image = self.inactive_image
        
    def draw(self, screen):
        screen.blit(self.image, (self.x + self.width/2 - self.image.get_width()/2, self.y + self.height/2 - self.image.get_height()/2))
        
    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.is_clicked(pos[0], pos[1]):
                self.image = self.active_image
            else:
                self.image = self.inactive_image
    
    def refresh(self):
        self.image = self.inactive_image
        
class BorderlessTextButton(BorderlessButton):
    def __init__(self, x, y, width, height, text, color, font, brighten_level = 0, sfx=None):
        super().__init__(x, y, width, height, sfx)
        self.text = text
        self.inactive_color = color
        self.active_color = tuple(x+brighten_level if x+brighten_level < 255 else 254 for x in color)
        self.color = self.inactive_color
        self.text_font = font

    def draw(self, screen):
        txt = self.text_font.render(self.text, 1, self.color)
        screen.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2))
                
    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.is_clicked(pos[0], pos[1]):
                self.color = self.active_color
            else:
                self.color = self.inactive_color
    
    def refresh(self):
        self.color = self.inactive_color
                