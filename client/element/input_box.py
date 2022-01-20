import pygame as pg
from pygame import mixer
from element.element_interface import ElementInterface

class InputBox(ElementInterface):
    def __init__(self, x, y, w, h, color, font, text="",  brigten_level=0, 
                 font_color=(255, 255, 255), border_color=(255,255,255), border_witdh = 2, sfx=None):
        self.border_witdh = border_witdh
        self.rect = pg.Rect(x, y, w, h)
        self.border_rect = pg.Rect(x + self.border_witdh, y + self.border_witdh, w - self.border_witdh * 2, h - self.border_witdh * 2)
        self.active_color = tuple(x+brigten_level for x in color)
        self.inactive_color = color
        self.color = self.inactive_color
        self.border_color = border_color
        self.font_color = font_color
        self.text = text
        self.font = font
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False
        self.sfx = sfx

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.active_color if self.active else self.inactive_color
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    if self.sfx is not None:
                        sound = mixer.Sound(self.sfx)
                        volume = mixer.music.get_volume()
                        sound.set_volume(volume if volume == 0 else volume + 0.2)
                        sound.play()
                    self.text = self.text[:-1]
                elif len(self.text) < 15:
                    key = event.unicode
                    if key.isalnum() or key.isalpha():
                        if self.sfx is not None:
                            sound = mixer.Sound(self.sfx)
                            volume = mixer.music.get_volume()
                            sound.set_volume(volume if volume == 0 else volume + 0.2)
                            sound.play()
                        mods = pg.key.get_mods()
                        if mods & pg.KMOD_LSHIFT or mods & pg.KMOD_CAPS:  
                            self.text += key
                        else:
                            self.text += key.lower()
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.font_color)

    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 0)
        pg.draw.rect(screen, self.border_color, self.border_rect, self.border_witdh)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    def refresh(self):
        self.color = self.inactive_color