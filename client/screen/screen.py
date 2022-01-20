"""
    Basic screen function
"""
class ScreenInterface:
    """
        Draw item on screen
    """
    def draw(self, screen):
        for atr in self.__dict__.values():
            atr.draw(screen)

    """
        Handle event that pygame detect
    """
    def handle_event(self, event):
        for atr in self.__dict__.values():
            atr.handle_event(event)

    """
        Return screen to new state
    """
    def refresh(self):
        for atr in self.__dict__.values():
            atr.refresh()