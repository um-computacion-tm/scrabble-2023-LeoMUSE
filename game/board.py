from game.cell import Cell
from game.dictionary import Dictionary

TW = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DW = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TL = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DL = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class Board:
    def __init__(self):
        self.grid = [[Cell('', 1) for _ in range(15) ]for _ in range(15)]
        self.set_multiplier()

    def set_multiplier_cord(self,cord, multiplier, multiplier_type):
        cell = self.grid[cord[0]][cord[1]]
        cell.multiplier = multiplier
        cell.multiplier_type = multiplier_type

    def set_multiplier(self):
        for cord in TW:
            self.set_multiplier_cord(cord, "word", 3)
        for cord in DW:
            self.set_multiplier_cord(cord, "word", 2)
        for cord in TL:
            self.set_multiplier_cord(cord, "letter", 3)
        for cord in DL:
            self.set_multiplier_cord(cord, "letter", 2)

    def calculate_word_value(self, word):
        value = 0
        word_multiplier = 1
        for cell in word:
            if cell.multiplier_type == "word" and cell.active:
                word_multiplier *= cell.multiplier
            value += cell.calculate_value()
            cell.active = False
        value *= word_multiplier
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
            
    def put_word(self, word, location, orientation):
        x, y = location

        for letter in word:
            self.grid[x][y].add_letter(letter)

            if orientation == 'H':
                y += 1
            elif orientation == 'V':
                x += 1

    def display_board(self, board):
            print("Tablero de Scrabble:")
            for row in board.grid:
                for cell in row:
                    if cell.multiplier_type == "word":
                        if cell.multiplier == 3:
                            print("[W,3]", end=' ')
                        elif cell.multiplier == 2:
                            print("[W,2]", end=' ')
                    elif cell.multiplier_type == "letter":
                        if cell.multiplier == 3:
                            print("[L,3]", end=' ')
                        elif cell.multiplier == 2:
                            print("[L,2]", end=' ')
                    else:
                        print("[   ]", end=' ')
                print()

    @property
    def is_empty(self):
        return not any(cell.letter for row in self.grid for cell in row)
    
if __name__ == '__main__':
    pass