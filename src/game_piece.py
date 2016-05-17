import pygame

class GamePiece(object):
    """
    Game piece class for PyChess
    """
    def __init__(self, name, color, image):
        self.name = name
        self.color = color
        self.image = image
        
    def get_name(self):
        """
        Function for returning the object's name
        """
        return self.name
        
    def get_color(self):
        """
        Function for returning the object's color
        """
        return self.color
           
    def get_image(self):
        """
        Function for returning the object's image
        """
        return self.image
        
    
        