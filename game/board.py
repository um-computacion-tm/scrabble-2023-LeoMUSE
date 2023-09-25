from game.cell import Cell
from game.dictionary import Dictionary

class Board:
    def __init__(self):
        self.grid = [[Cell('', 1) for _ in range(15) ]for _ in range(15)]

    def calculate_word_value(self,word):
        value = 0
        word_multiplier = 1
        for cell in word:
            if not(cell.multiplier_type) and cell.active:
                word_multiplier *= cell.multiplier
            value += cell.calculate_value()
            cell.active = False
        value = value * word_multiplier
        return value
    
    def validate_word_inside_board(self, word, location, orientation):
        x , y = location
        if orientation == 'H' and y + len(word) > 15:
            raise ValueError("La palabra no cabe en el tablero en la posicion especificada.")
        elif orientation == 'V' and x + len(word) > 15:
            raise ValueError("La palabra no cabe en el tablero en la posicion especificada.")
        return orientation in ('H', 'V')
    
    def check_word(self,word, file_path):
        wordletter = ""
        for _ in word:
            wordletter += _.letter.letter
        wordletter = wordletter.lower()
        with open(file_path, "r") as file:
            words = file.read().splitlines()
            if wordletter in words:
                return True
            else:
                return False
            
    def put_word_horizontal(self, word, location, orientation):
        x , y = location

        if orientation == 'H':
            for letter in word:
                self.grid[x][y].add_letter(letter)
                y += 1

    @property
    def is_empty(self):
        return not any(cell.letter for row in self.grid for cell in row)
    
if __name__ == '__main__':
    pass