from game.tile import Tile

class Cell:
    def __init__(self, multiplier:int , multiplier_type = None, letter = None, active = True, tile : Tile = None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.right_cell = None
        self.active = active
        self.tile = tile

    def add_letter(self, letter:str, row, col):
        self.letter = letter
        self.row = row
        self.col = col

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == "letter" and self.active:
            self.active = False
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def __str__(self):
        if self.letter is not None:
            return f"[{self.letter.letter}]"
        else:
            return "[ ]"
        
if __name__ == '__main__':
    pass