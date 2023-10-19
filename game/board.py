from game.cell import Cell
from game.dictionary import Dictionary
from game.tile import Tile

TW = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DW = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TL = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DL = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class Board:
    def __init__(self):
        self.grid = [[Cell('', 1) for _ in range(15) ]for _ in range(15)]
        self.set_multiplier()
        self.letter = None

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
        tiles = len(word)
        y, x = location
        if (orientation == 'H' and x + tiles > 15) or \
                (orientation == 'V' and y + tiles > 15):
            raise ValueError("Word out of board")
        return True
    
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
            
    def put_word_first_time(self, word, location, orientation):
        center = (7, 7)

        if orientation == "H":
            first_word = [(location[0], location[1] + i) for i in range(len(word))]
        elif orientation == "V":
            first_word = [(location[0] + i, location[1]) for i in range(len(word))]

        if center not in first_word:
            raise ValueError("The first word must be in the center")
        
        self.put_word(word, location, orientation)   
        return center in first_word
            
    def put_word(self, word, location, orientation):
        self.validate_word_inside_board(word, location, orientation)
        tiles = len(word)
        y, x = location
        fila, columna = (0, 1) if orientation == 'H' else (1, 0)

        for i in range(tiles):
            if self.grid[y][x].letter is None:
                self.grid[y][x].letter = word[i]
            y += fila
            x += columna

    def validate_word_connected(self, word, location, orientation):
        y, x = location
        count = 0
        cells = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]

        for direction in cells:
            dr, dc = direction 
            if 0 <= dr < 15 and 0 <= dc < 15 and self.grid[dr][dc].tile is not None:
                count += 1
            for _ in range(len(word)):
                if orientation == 'H':
                    x += 1
                elif orientation == 'V':
                    y += 1

        if count != 0:
            return True
        else:
            raise ValueError('Words must be connected')

    def display_board(self, board):
        print("Tablero de Scrabble:")
        print("  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14  ")

        for row in range(15):
            for col in range(15):
                self.print_cell_contents(row, col)
            print()

    def print_cell_contents(self, row, col):
        cell = self.grid[row][col]
        if (row, col) in TW:
            cell.multiplier_type = "word"
            cell.multiplier = 3
        elif (row, col) in DW:
            cell.multiplier_type = "word"
            cell.multiplier = 2
        elif (row, col) in TL:
            cell.multiplier_type = "letter"
            cell.multiplier = 3
        elif (row, col) in DL:
            cell.multiplier_type = "letter"
            cell.multiplier = 2

        if cell.letter is not None:
            print(f"[ {cell.letter.letter} ]", end=' ')
        elif cell.multiplier_type == "word":
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

    @property
    def is_empty(self):
        return not any(cell.letter for row in self.grid for cell in row)
    
if __name__ == '__main__':
    pass