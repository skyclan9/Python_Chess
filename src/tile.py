import pygame

class Tile(object):
    """
    Tile class for PyChess
    """
    def __init__(self, color):
        """
        Paramaters: 'green', 'white', and 'black'
        """
        self.color = color
        if self.color == "green":
            self.image = "../resources/green.png"
        elif self.color == "white":
            self.image = "../resources/white.png"
        elif self.color == "black":
            self.image = "../resources/black.jpg"
        else:
            raise ValueError()
        
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
        
    