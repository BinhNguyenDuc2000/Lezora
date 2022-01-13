class Player:
    OFFLINE_SATE = 0
    ONLINE_STATE = 1
    INGAME_STATE = 2

    def __init__(self, username):
        self.username = username
        self.password = ""
        self.state = Player.OFFLINE_SATE 

    def compare_player(self, player):
        if player.user_name == self.user_name and player.password == self.password:
            return True
        return False

    def player_to_string(self):
        data = ""
        data += self.username
        data += "_"
        data += str(self.state)
        return data

    def string_to_player(self, data):
        player_attribute = data.split("_")
        player =  Player(player_attribute[0])
        player.state =player_attribute[1]
        


if __name__ == "__main__":
    print(Player("").player_to_string())
