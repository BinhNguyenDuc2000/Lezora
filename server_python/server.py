import socket
from _thread import *
from player_list import PlayerList
from player import Player

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

player_list = PlayerList()

def threaded_client(conn):
    player = Player("")
    conn.send(str.encode(player.player_to_string()))
    while True:
        try:
            data = conn.recv(2048).decode().split("_")
            if (data[0] == "login"):
                player.username = data[1]
                player.password = data[2]
                for _player in player_list:
                    if player.compare_player(_player):
                        player.state = Player.ONLINE_STATE
            
            # conn.send(str.encode(player.player_to_string()))
            conn.send(str.encode("Hello"))
        except:
            break


    print("Lost connection")
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,))