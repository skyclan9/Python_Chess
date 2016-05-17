import pygame

class GameBoard(object):
    """
    Game Board class for PyChess
    """
    def __init__(self):
        self.width = 8
        self.height = 8
        self.tileArray = [[0 for x in range(self.width)] for y in range(self.height)]
        self.rectArray = [[0 for x in range(self.width)] for y in range(self.height)]
        
    def fill_tile_array(self):
        from tile import Tile
        whiteTile = Tile("white")
        blackTile = Tile("black")
        for i in range(8):
            for k in range(8):
                if i%2==0:
                    if k%2==0:
                        self.tileArray[i][k] = whiteTile
                    else:
                        self.tileArray[i][k] = blackTile
                else:
                    if k%2==0:
                        self.tileArray[i][k] = blackTile
                    else:
                        self.tileArray[i][k] = whiteTile