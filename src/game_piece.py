import pygame

class GamePiece:
    "Game Piece Class"
    def __init__(self, name, color, image):
        self.name = name
        self.color = color
        self.image = image
        
    def get_name(self):
        return self.name
        
    def get_color(self):
        return self.color
           
    def get_image(self):
        return self.image
        
    
        