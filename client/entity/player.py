
class Player():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.rank = 0
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_rank(self):
        return self.rank
    
    def set_rank(self, rank):
        self.rank = rank
    
    def set_player(self, username, password, rank):
        self.username = username
        self.password = password
        self.rank = rank
    