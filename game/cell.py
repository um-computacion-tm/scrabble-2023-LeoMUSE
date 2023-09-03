from game.tile import Tile

class Cell:
    def __init__(self, multiplier:int , multiplier_type:bool, letter = None, active = True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.right_cell = None
        self.active = active

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type and self.active:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value