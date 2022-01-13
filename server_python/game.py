class Game:
    def __init__(self, id):
        self.p1Went = False
        self.p2Went = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def game_to_string(self):
        game_string = str(self.id)
        game_string += "1" if self.p1Went else "0"
        game_string += "1" if self.p2Went else "0"
        game_string += "1" if self.ready else "0"
        game_string += "n" if self.moves[0] is None else self.moves[0]
        game_string += "n" if self.moves[1] is None else self.moves[1]
        game_string += str(self.wins[0])
        game_string += str(self.wins[1])
        game_string += str(self.ties)
        return game_string

    def string_to_game(self, game_string):
        self.id = int(game_string[0])
        self.p1Went = True if game_string[1] == "1" else False
        self.p2Went = True if game_string[2] == "1" else False
        self.ready = True if game_string[3] == "1" else False
        self.moves[0] = None if game_string[4] == "n" else game_string[4]
        self.moves[1] = None if game_string[5] == "n" else game_string[5]
        self.wins[0] = int(game_string[6])
        self.wins[1] = int(game_string[7])
        self.ties = int(game_string[8])
        

    def get_player_move(self, p):
        """
        :param p: [0,1]
        :return: Move
        """
        return self.moves[p]

    def play(self, player, move):
        self.moves[player] = move
        if player == 0:
            self.p1Went = True
        else:
            self.p2Went = True

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went

    def winner(self):

        p1 = self.moves[0].upper()[0]
        p2 = self.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1

        return winner

    def resetWent(self):
        self.p1Went = False
        self.p2Went = False
