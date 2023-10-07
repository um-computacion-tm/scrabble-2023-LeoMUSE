from game.tile import Tile

class Cell:
    def __init__(self, multiplier:int , multiplier_type = None, letter = None, active = True):
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
        if self.multiplier_type == "letter" and self.active:
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