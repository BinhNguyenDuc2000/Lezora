from element.element_interface import ElementInterface
from element.card import Card

class CardList(ElementInterface):
    def __init__(self, card1: Card, card2: Card, card3: Card, card4: Card):
        super().__init__()
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4 
        
    def draw(self, screen):
        for value in self.__dict__.values():
            value.draw(screen)
            
    def handle_event(self, event):
        for value in self.__dict__.values():
            value.handle_event(event)
            
    def refresh(self):
        for value in self.__dict__.values():
            value.refresh()
            
    def is_clicked(self, x, y):
        for value in self.__dict__.values():
            if value.is_clicked(x, y):
                return True
        return False
    
    def get_clicked(self, x, y):
        for value in self.__dict__.values():
            if value.is_clicked(x, y):
                return value
        return None
    
    