class Player:
    """
    Player class for PyChess
    """
    def __init__(self, name):
        self.width = 8
        self.height = 2
        self.piece_array = [[0 for x in range(self.width)] for y in range(self.height)]
        self.player_name = name

    def initialize_pieces(self):
        """
        Function call for initializing game
        pieces of a Player object
        """
        for w in range(self.width):
            for h in range(self.height):
                print("Initializing Pieces")
