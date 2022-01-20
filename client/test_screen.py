from screen.login_screen import LoginScreen
from screen.menu_screen import MenuScreen
from screen.loading_screen import LoadingScreen
from screen.register_screen import RegisterScreen
from screen.game_screen import GameScreen
from screen.error_screen import LoginErrorScreen
from screen.screen import ScreenInterface
from screen.config import DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, MAX_VOLUME, MIN_VOLUME
from screen.in_game_menu_screen import InGameMenuScreen
import pygame as pg
from pygame import mixer
import typer 

app = typer.Typer()


"""
        Testing screen
"""
def test_screen(current_screen: ScreenInterface):
    pg.mixer.init()
    pg.init()
    mixer.music.load("asset/music/Neon_Beach_Cloud_City_instrumental_2_52.mp3")
    mixer.music.set_volume(MAX_VOLUME)
    mixer.music.play(-1)
    mixer.music.set_volume(MAX_VOLUME)
    screen = pg.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT))
    pg.display.set_caption("Lezora")
    clock = pg.time.Clock()
    current_screen.fade_in(screen)
    done = False
    while not done:
        clock.tick(60)
        
        # Check to display which button
        if mixer.music.get_volume() > MIN_VOLUME:
            current_screen.sound_button = current_screen.mute_sound_button
        else:
            current_screen.sound_button = current_screen.unmute_sound_button
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                exit()  
            
            # Let screen handle event  
            current_screen.handle_event(event)
                        
        current_screen.draw(screen)
        pg.display.flip()
        clock.tick(30)
    
@app.command()
def menu():
    menu_screen = MenuScreen()
    test_screen(menu_screen)
    
@app.command()
def in_game_menu():
    in_game_menu_screen = InGameMenuScreen("123456789012345", 123)
    test_screen(in_game_menu_screen)

@app.command()
def loading():
    loading_screen = LoadingScreen()
    test_screen(loading_screen)
    
@app.command()
def login():
    login_screen = LoginScreen()
    test_screen(login_screen)
    
@app.command()
def register():
    register_screen = RegisterScreen()
    test_screen(register_screen)
    
@app.command()
def game():
    game_screen = GameScreen()
    # game_screen.show_helper_message("Testing")
    # game_screen.hide_helper_message()
    game_screen.set_eye_button("pass")
    game_screen.update_player_board_def("board_binh_30_20_0_0_0_20_3_1_2_1_3_2_3_0".split("_"))
    game_screen.update_opponent_board_atk("board_an_0_20_0_0_0_20_2_1_0_2_3_0_1_0".split("_"))
    
    test_screen(game_screen)
    
@app.command()
def login_error():
    login_error_screen = LoginErrorScreen("PLAYERALREADYONLINE")
    test_screen(login_error_screen)
    
    
if __name__ == "__main__":
    app()

