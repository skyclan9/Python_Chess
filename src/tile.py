import pygame

class Tile:
    'Tile Class'
    def __init__(self, color, image):
        self.color = color
        self.image = image
        
    def get_color(self):
        return self.color
        
    def get_image(self):
        return self.image
        
    