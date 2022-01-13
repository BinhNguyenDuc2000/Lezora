import pygame as pg
from color_constant import colors
from network import Network
from error_screen import ErrorScreen
from loading_screen import LoadingScreen
from menu_screen import MenuScreen
from login_screen import LoginScreen
from register_screen import RegisterScreen

def main():
    clock = pg.time.Clock()
    done = False
    
    n = Network()
    if n.server_msg is None:
        current_screen = ErrorScreen("Can't connect to server")
    else:
        current_screen = menu_screen

    while not done:
        clock.tick(60)
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
                        n = Network()
                        screen.fill(colors['dodgerblue4'])
                        loading_screen.draw(screen)
                        pg.display.flip()
                        pg.time.wait(1000)
                        if n.server_msg is not None:
                            current_screen = menu_screen

            if current_screen.__class__.__name__ == "MenuScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.login_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = login_screen
                    elif current_screen.register_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = register_screen

            if current_screen.__class__.__name__ == "LoginScreen" :
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.back_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = menu_screen    
                    if current_screen.submit_button.is_clicked(pos[0], pos[1]):
                        player_data = "login_" + current_screen.username_box.text + "_" + current_screen.password_box.text
                        res = n.send(player_data)
                        if res is None:
                            current_screen = ErrorScreen("Can't connect to server")    
                        else:
                            print(res)

            if current_screen.__class__.__name__ == "RegisterScreen":     
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.back_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = menu_screen   
        
        screen.fill(colors['dodgerblue4'])
        current_screen.draw(screen)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((640, 400))
    screen.fill(colors["green4"])
    menu_screen = MenuScreen()
    login_screen = LoginScreen()
    register_screen = RegisterScreen()
    loading_screen = LoadingScreen()
    main()