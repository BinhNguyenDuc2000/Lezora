from element.button import TextButton
from element.borderless_button import BorderlessPictureButton, BorderlessTextButton
from element.card import Card
from element.color_constant import colors
from screen.screen import ScreenInterface
from screen.config import CLICK_SFX, DEFAULT_FONT_SMALL, DEFAULT_FONT_VERY_SMALL, DEFAULT_SCREEN_COLOR, DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, cards
import pygame as pg

class GameScreen(ScreenInterface):
    def __init__(self):
        super().__init__()
        self.board_image = BorderlessPictureButton(0, 0, 640, 400, pg.image.load("asset/sprite/board.png"))
        self.quit_button = TextButton(0, 0, 60, 60, "Quit", colors["purple"], DEFAULT_FONT_SMALL, 
                                      brighten_level=30, font_color=colors["darkpink"], 
                                      border_color=colors["darkpink"], sfx=CLICK_SFX)
        self.hide_helper_card()
        self.hide_helper_message()
        
        self.wait_eye = BorderlessTextButton(390, 180, 40, 40, "wait", colors["silver"], DEFAULT_FONT_SMALL)
        self.pass_eye = BorderlessTextButton(390, 180, 40, 40, "pass", colors["silver"], DEFAULT_FONT_SMALL, brighten_level=30, sfx=CLICK_SFX)
        self.eye_button = None
        self.set_eye_button("wait")
        
        
    def set_eye_button(self, command):
        if self.eye_button is None or command != self.eye_button.text:
            if command == "wait":
                self.eye_button = self.wait_eye
            else:
                self.eye_button = self.pass_eye
         
        
    def show_helper_message(self, message):
        self.helper_message = TextButton(20, 150, 600, 100, message, colors["purple"], font=DEFAULT_FONT_SMALL, 
            border_color=colors["darkpink"], font_color=colors["darkpink"])
        
    def hide_helper_message(self):
        self.helper_message = None
        
    def update_player_board_atk(self, player_board):
        sfx = CLICK_SFX if self.eye_button.text != "wait" else None
        brighten_level = 30 if self.eye_button.text != "wait" else 0
        username = player_board[1]
        rank = player_board[2]
        hp = player_board[3]
        res = player_board[4]
        atk = player_board[5]
        tired_factor = player_board[7]
        card1 = player_board[8]
        card_status1 = player_board[9]
        card2 = player_board[10]
        card_status2 = player_board[11]
        card3 = player_board[12]
        card_status3 = player_board[13]
        card4 = player_board[14] 
        card_status4 = player_board [15]
        
        self.player_username = BorderlessTextButton(420, 320, 120, 60, username + "-" + rank, colors["white"]
                                                    , font=DEFAULT_FONT_VERY_SMALL)
        self.player_hp = BorderlessTextButton(570, 320, 40, 40, hp, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.player_res = BorderlessTextButton(580, 250, 30, 30, res, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.player_tired_factor = BorderlessTextButton(520, 250, 30, 30, tired_factor, 
                                                        colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.player_combat = TextButton(458, 248, 32, 32, atk, colors["pink"], font=DEFAULT_FONT_SMALL,
                                     font_color=colors["white"], border_color=colors["darkpink"])
        
        self.player_card1 = Card(80, 300, 60, 80, colors["white"], cards[card1], card_status1, brighten_level=brighten_level, sfx=sfx)
        
        self.player_card2 = Card(160, 300, 60, 80, colors["white"], cards[card2], card_status2, brighten_level=brighten_level, sfx=sfx)
        
        self.player_card3 = Card(240, 300, 60, 80, colors["white"], cards[card3], card_status3, brighten_level=brighten_level, sfx=sfx)
        
        self.player_card4 = Card(320, 300, 60, 80, colors["white"], cards[card4], card_status4, brighten_level=brighten_level, sfx=sfx)
        
    def update_player_board_def(self, player_board):
        sfx = CLICK_SFX if self.eye_button.text != "wait" else None
        brighten_level = 30 if self.eye_button.text != "wait" else 0
        
        username = player_board[1]
        rank = player_board[2]
        hp = player_board[3]
        res = player_board[4]
        defend = player_board[6]
        tired_factor = player_board[7]
        card1 = player_board[8]
        card_status1 = player_board[9]
        card2 = player_board[10]
        card_status2 = player_board[11]
        card3 = player_board[12]
        card_status3 = player_board[13]
        card4 = player_board[14] 
        card_status4 = player_board [15]
        
        self.player_username = BorderlessTextButton(420, 320, 120, 60, username + "-" + rank, colors["white"]
                                                    , font=DEFAULT_FONT_VERY_SMALL)
        self.player_hp = BorderlessTextButton(570, 320, 40, 40, hp, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.player_res = BorderlessTextButton(580, 250, 30, 30, res, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.player_tired_factor = BorderlessTextButton(520, 250, 30, 30, tired_factor, 
                                                        colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.player_combat = TextButton(458, 248, 32, 32, defend, colors["blue"], font=DEFAULT_FONT_SMALL,
                                     font_color=colors["white"], border_color=colors["darkpink"])
        
        self.player_card1 = Card(80, 300, 60, 80, colors["white"], cards[card1], card_status1, brighten_level=brighten_level, sfx=sfx)
        
        self.player_card2 = Card(160, 300, 60, 80, colors["white"], cards[card2], card_status2, brighten_level=brighten_level, sfx=sfx)
        
        self.player_card3 = Card(240, 300, 60, 80, colors["white"], cards[card3], card_status3, brighten_level=brighten_level, sfx=sfx)
        
        self.player_card4 = Card(320, 300, 60, 80, colors["white"], cards[card4], card_status4, brighten_level=brighten_level, sfx=sfx)
        
    
    def update_opponent_board_atk(self, opponent_board):
        username = opponent_board[1]
        rank = opponent_board[2]
        hp = opponent_board[3]
        res = opponent_board[4]
        atk = opponent_board[5]
        tired_factor = opponent_board[7]
        card1 = opponent_board[8]
        card_status1 = opponent_board[9]
        card2 = opponent_board[10]
        card_status2 = opponent_board[11]
        card3 = opponent_board[12]
        card_status3 = opponent_board[13]
        card4 = opponent_board[14] 
        card_status4 = opponent_board [15]
        
        self.opponent_username = BorderlessTextButton(420, 40, 120, 60, username + "-" + rank, colors["white"]
                                                    , font=DEFAULT_FONT_VERY_SMALL)
        self.opponent_hp = BorderlessTextButton(570, 40, 40, 40, hp, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.opponent_res = BorderlessTextButton(580, 120, 30, 30, res, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.opponent_tired_factor = BorderlessTextButton(520, 120, 30, 30, tired_factor, 
                                                        colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.opponent_combat = TextButton(458, 118, 32, 32, atk, colors["pink"], font=DEFAULT_FONT_SMALL,
                                     font_color=colors["white"], border_color=colors["darkpink"])
        
        if card_status1 != "0":
            self.opponent_card1 = Card(80, 20, 60, 80, colors["white"], cards[card1], card_status1)
        else:
            self.opponent_card1 = Card(80, 20, 60, 80, colors["white"], cards["-1"], card_status1)
        
        if card_status2 != "0":
            self.opponent_card2 = Card(160, 20, 60, 80, colors["white"], cards[card2], card_status2)
        else:
            self.opponent_card2 = Card(160, 20, 60, 80, colors["white"], cards["-1"], card_status2)
        
        if card_status3 != "0":
            self.opponent_card3 = Card(240, 20, 60, 80, colors["white"], cards[card3], card_status3)
        else:
            self.opponent_card3 = Card(240, 20, 60, 80, colors["white"], cards["-1"], card_status3)
        
        if card_status4 != "0":
            self.opponent_card4 = Card(320, 20, 60, 80, colors["white"], cards[card4], card_status4)
        else:
            self.opponent_card4 = Card(320, 20, 60, 80, colors["white"], cards["-1"], card_status4)
        
    def update_opponent_board_def(self, opponent_board):
        username = opponent_board[1]
        rank = opponent_board[2]
        hp = opponent_board[3]
        res = opponent_board[4]
        defend = opponent_board[6]
        tired_factor = opponent_board[7]
        card1 = opponent_board[8]
        card_status1 = opponent_board[9]
        card2 = opponent_board[10]
        card_status2 = opponent_board[11]
        card3 = opponent_board[12]
        card_status3 = opponent_board[13]
        card4 = opponent_board[14] 
        card_status4 = opponent_board [15]
        
        self.opponent_username = BorderlessTextButton(420, 40, 120, 60, username + "-" + rank, colors["white"]
                                                    , font=DEFAULT_FONT_VERY_SMALL)
        self.opponent_hp = BorderlessTextButton(570, 40, 40, 40, hp, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.opponent_res = BorderlessTextButton(580, 120, 30, 30, res, colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.opponent_tired_factor = BorderlessTextButton(520, 120, 30, 30, tired_factor, 
                                                        colors["darkpink"], font=DEFAULT_FONT_SMALL)
        
        self.opponent_combat = TextButton(458, 118, 32, 32, defend, colors["blue"], font=DEFAULT_FONT_SMALL,
                                     font_color=colors["white"], border_color=colors["darkpink"])
        
        if card_status1 != "0":
            self.opponent_card1 = Card(80, 20, 60, 80, colors["white"], cards[card1], card_status1)
        else:
            self.opponent_card1 = Card(80, 20, 60, 80, colors["white"], cards["-1"], card_status1)
        
        if card_status2 != "0":
            self.opponent_card2 = Card(160, 20, 60, 80, colors["white"], cards[card2], card_status2)
        else:
            self.opponent_card2 = Card(160, 20, 60, 80, colors["white"], cards["-1"], card_status2)
        
        if card_status3 != "0":
            self.opponent_card3 = Card(240, 20, 60, 80, colors["white"], cards[card3], card_status3)
        else:
            self.opponent_card3 = Card(240, 20, 60, 80, colors["white"], cards["-1"], card_status3)
        
        if card_status4 != "0":
            self.opponent_card4 = Card(320, 20, 60, 80, colors["white"], cards[card4], card_status4)
        else:
            self.opponent_card4 = Card(320, 20, 60, 80, colors["white"], cards["-1"], card_status4)
        
    def draw(self, screen):
        screen.fill(DEFAULT_SCREEN_COLOR)
        self.board_image.draw(screen)
        for key, value in self.__dict__.items():
            if key != "mute_sound_button" and key != "unmute_sound_button" and key != "board_image" and key != "helper_message" and key != "helper_card" and key != "wait_eye" and key != "pass_eye":
                if value is not None:
                    value.draw(screen)
        
        if self.helper_message is not None:
            self.helper_message.draw(screen)
            
        if self.helper_card is not None:
            self.helper_card.draw(screen)
                    
    def show_helper_card(self, card):
        self.helper_card = Card(45, 120, 120, 160, colors["white"],
                                 pg.transform.scale(card.inactive_image, (120, 160)), 
                                 status=0)
        
    def hide_helper_card(self):
        self.helper_card = None
                    
    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pg.MOUSEMOTION:
            pos = pg.mouse.get_pos()
            for key, value in self.__dict__.items():           
                if value is not None:          
                    if value.__class__.__name__ == "Card":
                        if value.is_clicked(pos[0], pos[1]):
                            self.show_helper_card(value)
                            return              
        self.hide_helper_card()
                    
    def refresh(self):
        super().refresh()
        
        self.hide_helper_card()
        self.hide_helper_message()
        
        # self.player_username = None
        
        # self.opponent_username = None
        
        # self.helper_message = None
                    
    
        
    