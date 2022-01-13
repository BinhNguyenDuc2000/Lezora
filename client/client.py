import pygame as pg
from color_constant import colors
from network import Network
from menu_screen import MenuScreen
from login_screen import LoginScreen

def main():
    clock = pg.time.Clock()
    done = False
    
    # n = Network()
    # print(n.server_msg)
    # if n.server_msg is None:
    #     exit()

    current_screen = menu_screen

    while not done:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                exit()  

            # Let screen handle event  
            current_screen.handle_event(event)

            if current_screen.__class__.__name__ == "MenuScreen":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    if current_screen.login_button.is_clicked(pos[0], pos[1]):
                        current_screen.refresh()
                        current_screen = login_screen

            if current_screen.__class__.__name__ == "LoginScreen":
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
    main()