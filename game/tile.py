class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.letter == other.letter and self.value == other.value
        return False
    
    def __hash__(self):
        return hash((self.letter, self.value))

    def __repr__(self):
        return f"Tile('{self.letter}',{self.value})"
    
if __name__ == '__main__':
    pass