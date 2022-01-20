import pygame as pg
from pygame import mixer
from network import Network

from screen.error_screen import ErrorScreen, LoginErrorScreen, RegisterErrorScreen, InGameMenuErrorScreen
from screen.game_screen import GameScreen
from screen.enter_room_id_screen import EnterRoomIDScreen
from screen.loading_screen import LoadingScreen
from screen.menu_screen import MenuScreen
from screen.login_screen import LoginScreen
from screen.register_screen import RegisterScreen
from screen.in_game_menu_screen import InGameMenuScreen
from screen.config import DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, MAX_VOLUME

from entity.player import Player

def main():
    pg.mixer.init()
    pg.init()
    screen = pg.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT))
    pg.display.set_caption("Lezora")
    clock = pg.time.Clock()
    done = False
    game_start = False
    screen = pg.display.set_mode((DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT))
    pg.display.flip()
    
    menu_screen = MenuScreen()
    in_game_menu_screen = None
    enter_room_id_screen = EnterRoomIDScreen()
    game_screen = None
    player = Player()
    login_screen = LoginScreen()
    register_screen = RegisterScreen()
    player_index = 0
    opponent_index = 0
    
    try:
        n = Network()
        if n.server_msg is None:
            current_screen = ErrorScreen("Can't connect to server")
            current_screen.fade_in(screen)
        else:
            
            current_screen = menu_screen
            current_screen.fade_in(screen)
            
    
    except:
        current_screen = ErrorScreen("Can't connect to server")
        current_screen.fade_in(screen)

    mixer.music.load("asset/music/Neon_Beach_Cloud_City_instrumental_2_52.mp3")
    mixer.music.set_volume(MAX_VOLUME)
    mixer.music.play(-1)
    mixer.music.set_volume(MAX_VOLUME)
    
    time_elapsed_since_last_action = 0
    
    while not done:
        dt = clock.tick(30)
        
        time_elapsed_since_last_action += dt
        if time_elapsed_since_last_action > 180:
            time_elapsed_since_last_action = 0
            if current_screen.__class__.__name__ == "GameScreen":
                if not game_start:
                    try:
                        res = n.send("getroom")
                        if res is None:
                            game_start = False
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                        else:
                            res = res.split("_")
                            if (res[0] == "waiting"):
                                pass
                            elif (res[0] == "ready"):
                                current_screen.show_helper_message("Ready game ID:" + res[1])
                                current_screen.draw(screen)
                                pg.display.flip()
                                pg.time.wait(1500)
                                current_screen.refresh()
                                current_screen.draw(screen)
                                pg.display.flip()
                                game_start = True
                                
                            elif  (res[0] == "closed"):
                                current_screen.show_helper_message("Game closed")
                                current_screen.draw(screen)
                                game_start = False
                                pg.display.flip()
                                pg.time.wait(1500)
                                current_screen.refresh()
                                current_screen = in_game_menu_screen
                                current_screen.fade_in(screen)
                                
                            else:
                                raise Exception("Can't connect to server")
                    except:
                        current_screen.refresh()
                        game_start = False
                        current_screen = ErrorScreen("Can't connect to server")
                        current_screen.fade_in(screen)
                        
                        
                else:
                    try: 
                        res = n.send("getgame")
                        
                        if res is None:
                            game_start = False
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                        else:
                            res = res.split("_")
                            if (res[0] == "win"):
                                if (int(res[1]) == player_index):
                                    current_screen.show_helper_message("You win")
                                    current_screen.draw(screen)
                                    game_start = False                               
                                    pg.display.flip()
                                    pg.time.wait(1500)
                                    current_screen.refresh()
                                    current_screen = in_game_menu_screen
                                    current_screen.fade_in(screen) 
                                    
                                else:
                                    current_screen.show_helper_message("You lose")
                                    current_screen.draw(screen)
                                    game_start = False
                                    pg.display.flip()
                                    pg.time.wait(1500)
                                    current_screen.refresh()
                                    current_screen = in_game_menu_screen
                                    current_screen.fade_in(screen)
                            
                            if (res[0] == "tie"):                               
                                current_screen.show_helper_message("Tie")
                                current_screen.draw(screen)
                                game_start = False                               
                                pg.display.flip()
                                pg.time.wait(1500)
                                current_screen.refresh()
                                current_screen = in_game_menu_screen
                                current_screen.fade_in(screen)  
                                    
                            elif  (res[0] == "closed"):
                                current_screen.show_helper_message("Game closed")
                                current_screen.draw(screen)
                                game_start = False
                                pg.display.flip()
                                pg.time.wait(1500)
                                current_screen.refresh()
                                current_screen = in_game_menu_screen
                                current_screen.fade_in(screen) 
                            
                            elif (res[0] == "atk"):
                                print(player_index)
                                if (int(res[1]) == player_index):
                                    current_screen.set_eye_button("pass")
                                    player_board = n.send("getboard_"+str(player_index))
                                    if player_board is None:
                                        raise Exception("Can't connect to server")
                                    player_board = player_board.split("_")
                                    current_screen.update_player_board_atk(player_board)
                                    
                                    opponent_board =  n.send("getboard_"+str(opponent_index))
                                    if opponent_board is None:
                                        raise Exception("Can't connect to server")
                                    opponent_board = opponent_board.split("_")
                                    current_screen.update_opponent_board_def(opponent_board)
                                    
                                    current_screen.draw(screen)
                                else:
                                    current_screen.set_eye_button("wait")
                                    player_board = n.send("getboard_"+str(player_index))
                                    if player_board is None:
                                        raise Exception("Can't connect to server")
                                    player_board = player_board.split("_")
                                    current_screen.update_player_board_def(player_board)
                                    
                                    opponent_board =  n.send("getboard_"+str(opponent_index))
                                    if opponent_board is None:
                                        raise Exception("Can't connect to server")
                                    opponent_board = opponent_board.split("_")
                                    current_screen.update_opponent_board_atk(opponent_board)
                                    
                                    current_screen.draw(screen)
                                    
                            elif (res[0] == "def"):
                                if (int(res[1]) == player_index):
                                    current_screen.set_eye_button("pass")
                                    player_board = n.send("getboard_"+str(player_index))
                                    if player_board is None:
                                        raise Exception("Can't connect to server")
                                    player_board = player_board.split("_")
                                    current_screen.update_player_board_def(player_board)
                                    
                                    opponent_board =  n.send("getboard_"+str(opponent_index))
                                    if opponent_board is None:
                                        raise Exception("Can't connect to server")
                                    opponent_board = opponent_board.split("_")
                                    current_screen.update_opponent_board_atk(opponent_board)
                                    
                                    current_screen.draw(screen)
                                    
                                else:
                                    current_screen.set_eye_button("wait")
                                    player_board = n.send("getboard_"+str(player_index))
                                    if player_board is None:
                                        raise Exception("Can't connect to server")
                                    player_board = player_board.split("_")
                                    current_screen.update_player_board_atk(player_board)
                                    
                                    opponent_board =  n.send("getboard_"+str(opponent_index))
                                    if opponent_board is None:
                                        raise Exception("Can't connect to server")
                                    opponent_board = opponent_board.split("_")
                                    current_screen.update_opponent_board_def(opponent_board)
                                    
                                    current_screen.draw(screen)
                                    
                                
                    except Exception as e:
                        game_start = False
                        current_screen.refresh()
                        current_screen = ErrorScreen("Can't connect to server")
                        current_screen.fade_in(screen)
                    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                exit()  

            # Let screen handle event  
            current_screen.handle_event(event)

            if current_screen.__class__.__name__ == "ErrorScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.try_again_button.is_clicked(pos[0], pos[1]):
                        try:
                            current_screen = LoadingScreen("Connecting to server")
                            current_screen.fade_in(screen)
                            pg.display.flip()
                            n = Network()                  
                            if n.server_msg is not None:
                                current_screen.refresh()
                                current_screen = menu_screen
                                current_screen.fade_in(screen)
                        except: 
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                            
            elif current_screen.__class__.__name__ == "LoginErrorScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.try_again_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = login_screen
                        current_screen.fade_in(screen)
                        
            elif current_screen.__class__.__name__ == "RegisterErrorScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.try_again_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = register_screen
                        current_screen.fade_in(screen)
                        
            elif current_screen.__class__.__name__ == "InGameMenuErrorScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.try_again_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = in_game_menu_screen
                        current_screen.fade_in(screen)

            elif current_screen.__class__.__name__ == "MenuScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.login_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = login_screen
                        current_screen.fade_in(screen)
                    elif current_screen.register_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = register_screen
                        current_screen.fade_in(screen)

            elif current_screen.__class__.__name__ == "LoginScreen" :
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.back_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = menu_screen  
                        current_screen.fade_in(screen)  
                    elif current_screen.submit_button.is_clicked(pos[0], pos[1]):
                        player_data = "login_" + current_screen.username_box.text + "_" + current_screen.password_box.text
                        try:
                            res = n.send(player_data)                           
                            if res is None:
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")   
                                current_screen.fade_in(screen) 
                            else:
                                res = res.split("_")
                                if res[0] == "error":
                                    current_screen.refresh()
                                    current_screen = LoginErrorScreen(res[1])
                                    current_screen.fade_in(screen)
                                if res[0] == "player":
                                    current_screen.refresh()
                                    player.set_player(res[1], res[2], res[3])
                                    in_game_menu_screen = InGameMenuScreen(player.get_username(), player.get_rank())
                                    current_screen = in_game_menu_screen
                                    current_screen.fade_in(screen)
                        except:
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                            

            elif current_screen.__class__.__name__ == "RegisterScreen":     
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.back_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = menu_screen
                        current_screen.fade_in(screen)
                    elif current_screen.submit_button.is_clicked(pos[0], pos[1]):
                            player_data = "register_" + current_screen.username_box.text + "_" + current_screen.password_box.text
                            try:
                                res = n.send(player_data)                               
                                if res is None:
                                    current_screen.refresh()
                                    current_screen = ErrorScreen("Can't connect to server")
                                    current_screen.fade_in(screen)    
                                else:
                                    res = res.split("_")
                                    if res[0] == "error":
                                        current_screen.refresh()
                                        current_screen = RegisterErrorScreen(res[1])   
                                        current_screen.fade_in(screen)
                                    if res[0] == "player":
                                        current_screen.refresh()
                                        player.set_player(res[1], res[2], res[3])
                                        in_game_menu_screen = InGameMenuScreen(player.get_username(), player.get_rank())
                                        current_screen = in_game_menu_screen
                                        current_screen.fade_in(screen)
                            except:
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)
                                
            elif current_screen.__class__.__name__ == "InGameMenuScreen":     
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.logout_button.is_clicked(pos[0], pos[1]):
                        try:
                            res = n.send("logout")
                            if res is None:
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)
                            if res == "logout":
                                current_screen.refresh()
                                current_screen = menu_screen
                                current_screen.fade_in(screen)
                        except:
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                    elif current_screen.create_room_button.is_clicked(pos[0], pos[1]):
                        try:
                            res = n.send("createroom")
                            if res is None:
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)
                            else:
                                res = res.split("_")
                                if (res[0] == "waiting"):
                                    current_screen.refresh()
                                    player_index = 1
                                    opponent_index = 2
                                    game_screen = GameScreen()
                                    game_screen.show_helper_message("Waiting game ID:" + res[1])
                                    current_screen = game_screen
                                    current_screen.fade_in(screen)
                        except Exception as e:
                            print(e)
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                            
                    elif current_screen.join_room_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = enter_room_id_screen
                        current_screen.fade_in(screen)
            
            elif current_screen.__class__.__name__ == "EnterRoomIDScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()  
                    if current_screen.back_button.is_clicked(pos[0], pos[1]):
                        current_screen = in_game_menu_screen
                        current_screen.fade_in(screen)

                    elif current_screen.submit_button.is_clicked(pos[0], pos[1]):
                        try:
                            res = n.send("joinroom_" + current_screen.room_id_box.text)
                            if res is None:
                                game_start = False
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)
                            else:
                                res = res.split("_")
                                if (res[0] == "ready"):
                                    current_screen.refresh()
                                    player_index = 2
                                    opponent_index = 1
                                    game_screen = GameScreen()
                                    game_screen.show_helper_message("Ready game ID:" + res[1])
                                    current_screen = game_screen
                                    current_screen.fade_in(screen)
                                    pg.display.flip()
                                    pg.time.wait(1500)
                                    current_screen.refresh()
                                    current_screen.draw(screen)
                                    pg.display.flip()
                                    game_start = True
                                    
                                elif res[0] == "error":
                                    game_start = False
                                    current_screen.refresh()
                                    current_screen = InGameMenuErrorScreen(res[1])   
                                    current_screen.fade_in(screen)
                        except:
                            game_start = False
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
            
            elif current_screen.__class__.__name__ == "GameScreen":             
                 if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.quit_button.is_clicked(pos[0], pos[1]):
                        try:
                            res = n.send("quitroom")
                            if res is None:
                                raise Exception("Can't connect to server")
                            else:
                                res = res.split("_")
                                if (res[0] == "quitroom"):
                                    game_start = False
                                    current_screen.refresh()
                                    current_screen = in_game_menu_screen
                                    current_screen.fade_in(screen)
                                elif (res[0] == "win"):
                                    current_screen.show_helper_message("You lose")
                                    current_screen.draw(screen)
                                    game_start = False
                                    pg.display.flip()
                                    pg.time.wait(1500)
                                    game_screen.refresh()
                                    current_screen = in_game_menu_screen
                                    current_screen.fade_in(screen) 
                                else:
                                    raise Exception("Can't connect to server")
                        except:
                            game_start = False
                            current_screen.refresh()
                            current_screen = ErrorScreen("Can't connect to server")
                            current_screen.fade_in(screen)
                            
                    elif current_screen.eye_button.text != "wait":
                        if current_screen.eye_button.is_clicked(pos[0], pos[1]) :
                            try:
                                res = n.send("pass")
                                if res is None:
                                    raise Exception("Can't connect to server")
                                else:
                                    if res != "pass":
                                        raise Exception("Can't connect to server")
                            except:
                                game_start = False
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)

                        
                        elif current_screen.player_card1.is_clicked(pos[0], pos[1]) and current_screen.player_card1.status == "0":
                            try:
                                if event.button == 3: 
                                    res = n.send("sell_0")
                                else:
                                    res = n.send("use_0")
                                if res is None:
                                    raise Exception("Can't connect to server")
                                
                            except:
                                game_start = False
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)
                                
                        elif current_screen.player_card2.is_clicked(pos[0], pos[1]) and current_screen.player_card2.status == "0":
                            try:
                                if event.button == 3: 
                                    res = n.send("sell_1")
                                else:
                                    res = n.send("use_1")
                                if res is None:
                                    raise Exception("Can't connect to server")
                            except:
                                game_start = False
                                current_screen.refresh()
                                current_screen = ErrorScreen("Can't connect to server")
                                current_screen.fade_in(screen)
                                
                        elif current_screen.player_card3.is_clicked(pos[0], pos[1]) and current_screen.player_card3.status == "0":
                                try:
                                    if event.button == 3: 
                                        res = n.send("sell_2")
                                    else:
                                        res = n.send("use_2")
                                    if res is None:
                                        raise Exception("Can't connect to server")
                                except:
                                    game_start = False
                                    current_screen.refresh()
                                    current_screen = ErrorScreen("Can't connect to server")
                                    current_screen.fade_in(screen)
                        
                        elif current_screen.player_card4.is_clicked(pos[0], pos[1]) and current_screen.player_card4.status == "0":
                                try:
                                    if event.button == 3: 
                                        res = n.send("sell_3")
                                    else:
                                        res = n.send("use_3")
                                    if res is None:
                                        raise Exception("Can't connect to server")
                                except:
                                    game_start = False
                                    current_screen.refresh()
                                    current_screen = ErrorScreen("Can't connect to server")
                                    current_screen.fade_in(screen)                  


            
        current_screen.draw(screen)
        pg.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    pg.init()
    main()