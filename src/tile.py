import pygame

class Tile:
    """
    Tile class for PyChess
    """"
    def __init__(self, color, image):
        self.color = color
        self.image = image
        
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
        
    