import pygame as pg
from pygame import mixer
from element.button import Button

class Card(Button):
    def __init__(self, x, y, width, height, color, image, status, border_color=(255, 255, 255), brighten_level=0, sfx=None):
        super().__init__(x, y, width, height, color, border_color, brighten_level, sfx)
        self.BORDER_WIDTH = 5
        self.inactive_image = image
        self.active_image = image.copy()
        self.active_image.fill((brighten_level, brighten_level, brighten_level), special_flags=pg.BLEND_RGB_ADD)
        self.image = self.inactive_image
        self.status = status
        
    def set_border_color(self):
        if self.status == "0":
            self.border_color = (255, 255, 255)
        elif self.status == "1":
            self.border_color = (230, 142, 54)
        elif self.status == "2":
            self.border_color = (0, 0, 0)
        
    def draw(self, screen):
        self.set_border_color()
        pg.draw.rect(screen, self.border_color, (self.x-self.BORDER_WIDTH, self.y-self.BORDER_WIDTH, 
                                                 self.width + 2 * self.BORDER_WIDTH, 
                                                 self.height + 2 * self.BORDER_WIDTH), 0)
            
        screen.blit(self.image, 
                    (self.x + self.width/2 - self.image.get_width()/2, 
                     self.y + self.height/2 - self.image.get_height()/2))
        
    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.status == 0:
                if self.is_clicked(pos[0], pos[1]):
                    if self.sfx is not None:
                        sound = mixer.Sound(self.sfx)
                        volume = mixer.music.get_volume()
                        sound.set_volume(volume if volume == 0 else volume + 0.2)
                        sound.play()
                    self.image = self.active_image
                else:
                    self.image = self.inactive_image
    
    def refresh(self):
        self.image = self.inactive_image