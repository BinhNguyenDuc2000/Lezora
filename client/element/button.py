import pygame as pg


class Button:

    def __init__(self, x, y, width, height, active_color, border_color=(255,255,255), inactive_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.color = inactive_color
        self.border_color = border_color
        self.BORDER_WIDTH = 2

    def draw(self, screen):
        pg.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), 0)
        pg.draw.rect(screen, self.color, (
        self.x + self.BORDER_WIDTH, self.y + self.BORDER_WIDTH, self.width - self.BORDER_WIDTH * 2,
        self.height - self.BORDER_WIDTH * 2), 0)

    def handle_event(self, event):
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            if self.is_clicked(pos[0], pos[1]):
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
    def __init__(self, x, y, width, height, text, active_color, border_color=(255,255,255), inactive_color=(0, 0, 0), font_color = (255, 255, 255)):
        super().__init__(x, y, width, height, active_color, border_color, inactive_color)
        self.text = text
        self.font_color = font_color
        self.text_font = pg.font.SysFont("comicsans", 30)

    def change_font_size(self, size):
        self.text_font = pg.font.SysFont("comicsans", size)

    def draw(self, screen):
        super().draw(screen)
        txt = self.text_font.render(self.text, 1, self.font_color)
        screen.blit(txt, (self.x + self.width/2 - txt.get_width()/2, self.y + self.height/2 - txt.get_height()/2))