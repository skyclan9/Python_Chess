import pygame

class GameBoard(object):
    """
    Game Board class for PyChess
    """
    def __init__(self):
        self.width = 8
        self.height = 8
        rectFill = pygame.Rect(0,0,0,0)
        self.tileArray = [["" for x in range(self.width)] for y in range(self.height)]
        self.rectArray = [[rectFill for x in range(self.width)] for y in range(self.height)]
        
    def fill_tileArray(self):
        white = "../resources/white.png"
        black = "../resources/black.jpg"
        for i in range(8):
            for k in range(8):
                if i%2==0:
                    if k%2==0:
                        self.tileArray[i][k] = black
                    else:
                        self.tileArray[i][k] = white
                else:
                    if k%2==0:
                        self.tileArray[i][k] = white
                    else:
                        self.tileArray[i][k] = black
                        
    def fill_rectArray(self):
        for i in range(8):
            for k in range(8):
                rect = pygame.Rect(90*k,632-90*i,90,90)
                self.rectArray[i][k] = rect
 