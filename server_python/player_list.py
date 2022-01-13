from player import Player
class PlayerList:
    def __init__(self, file_name = "player_data.txt"):
        self.player_list = {}
        with open(file_name, "rt") as file:
            for line in file:
                player_data = line.split("_")
                player = Player(player_data[0])
                player.password = player_data[1]
                self.player_list[player_data[0]] = player
    
    def get_player(self, username):
        return self.player_list[username]

if __name__ == "__main__":
    pl = PlayerList()
    print(pl.get_player("tuan").password)