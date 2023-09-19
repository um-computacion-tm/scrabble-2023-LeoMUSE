class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def __str__(self):
        return f"Tile('{self.letter}',{self.value})"
    
if __name__ == '__main__':
    pass