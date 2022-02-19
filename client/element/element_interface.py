class ElementInterface:
    """
        Draw element on screen
    """
    def draw(self, screen):
        pass
    
    """
        Handle event that pygame detect
    """
    def handle_event(self, event):
        pass
    
    """
        Return element to inactive state
    """
    def refresh(self):
        pass
   
    """
       If the element is clicked 
    """
    def is_clicked(self, x, y):
       pass