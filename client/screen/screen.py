import pygame as pg
from pygame import mixer
from screen.config import DEFAULT_SCREEN_COLOR, DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, MAX_VOLUME, MIN_VOLUME, CLICK_SFX
from element.borderless_button import BorderlessPictureButton

import webbrowser

"""
    Basic screen function
"""
class ScreenInterface:
    
    def __init__(self):
        self.question_button = BorderlessPictureButton(0, 320, 40, 40, pg.image.load("asset/sprite/question.png"), 30, sfx=CLICK_SFX)
        self.unmute_sound_button = BorderlessPictureButton(0, 360, 40, 40, pg.image.load("asset/sprite/nobell.png"), 30, sfx=CLICK_SFX)
        self.mute_sound_button = BorderlessPictureButton(0, 360, 40, 40, pg.image.load("asset/sprite/bell.png"), 30, sfx=CLICK_SFX)
        try:
            self.sound_button = self.mute_sound_button if mixer.music.get_volume() > MIN_VOLUME else self.unmute_sound_button
        except:
            pg.mixer.init()
            self.sound_button = self.mute_sound_button if mixer.music.get_volume() > MIN_VOLUME else self.unmute_sound_button
        
        
            
    """
        Darken screen by drawing on top a black screen with decreasing opacity
    """
    def fade_in(self, screen, width=DEFAULT_SCREEN_WIDTH, height=DEFAULT_SCREEN_HEIGHT):
        try:
            self.sound_button = self.mute_sound_button if mixer.music.get_volume() > MIN_VOLUME else self.unmute_sound_button
        except:
            pg.mixer.init()
            self.sound_button = self.mute_sound_button if mixer.music.get_volume() > MIN_VOLUME else self.unmute_sound_button
        fade = pg.Surface((width, height))
        fade.fill((0,0,0))
        for alpha in range(300, 0, -2):
            screen.fill(DEFAULT_SCREEN_COLOR)
            fade.set_alpha(alpha)
            self.draw(screen)
            screen.blit(fade, (0,0))
            pg.display.flip()
            pg.time.wait(5)

    """
        Draw all on element on screen
    """
    def draw(self, screen):
        screen.fill(DEFAULT_SCREEN_COLOR)
        for key, value in self.__dict__.items():
            if key != "mute_sound_button" and key != "unmute_sound_button":
                if value is not None:
                    value.draw(screen)

    """
        Handle event that pygame detect
    """
    def handle_event(self, event):
        for key, value in self.__dict__.items():
            if key != "mute_sound_button" and key != "unmute_sound_button":
                if value is not None:
                    value.handle_event(event)
        
        if event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if self.sound_button.is_clicked(pos[0], pos[1]):
                    if mixer.music.get_volume() > MIN_VOLUME:
                        mixer.music.set_volume(MIN_VOLUME)
                        self.sound_button = self.unmute_sound_button
                    else:
                        mixer.music.set_volume(MAX_VOLUME)
                        self.sound_button = self.mute_sound_button
                
                if self.question_button.is_clicked(pos[0], pos[1]):
                    webbrowser.open("https://docs.google.com/presentation/d/10GmPmx27uVzn10_yeLz9sgCPXRtgp0vuGG8SFdkBIFI/edit?usp=sharing")

    """
        Return all element to inactive state
    """
    def refresh(self):
        for key, value in self.__dict__.items():
            if key != "mute_sound_button" and key != "unmute_sound_button":
                if value is not None:
                    value.refresh()
            