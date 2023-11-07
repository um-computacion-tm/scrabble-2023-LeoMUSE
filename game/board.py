import copy
from game.cell import Cell
from game.tile import Tile
from game.dictionary import word_in_dictionary


class NoCenterLetterException(Exception):
    pass

class NoWordConnectedException(Exception):
    pass

class NoValidCrossWordException(Exception):
    pass

TW = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DW = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TL = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DL = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))

class Board:
    def __init__(self):
        self.grid = [[Cell('', 1) for _ in range(15) ]for _ in range(15)]
        self.set_multiplier()
        self.letter = None
        self.first_time = True

    @staticmethod
    def convert_word_to_tiles(word: str) -> list:
            letter_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}
            return [Tile(letter=letter, value=letter_values.get(letter, 0)) for letter in word]

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

    def calculate_word_value(self, word, location, orientation):
        value = 0
        word_multiplier = 1
        for cell in word:
            if cell.multiplier_type == "word" and cell.active:
                word_multiplier *= cell.multiplier
            tile_value = cell.calculate_value()
            if tile_value > 0:
                value += tile_value
            cell.active = False
        value *= word_multiplier
        return value
    
    def validate_word_inside_board(self, word, location, orientation):
        tiles = len(word)
        y, x = location
        if (orientation == 'H' and x + tiles > 15) or \
                (orientation == 'V' and y + tiles > 15):
            raise ValueError("Palabra fuera del tablero")
        return True
            
    def put_word_first_time(self, word, location, orientation):
        if self.first_time:
            self.validate_word_inside_board(word, location, orientation)
            center_position = (7, 7)
            if orientation == "H":
                word_positions = [(location[0], location[1] + i) for i in range(len(word))]
            elif orientation == "V":
                word_positions = [(location[0] + i, location[1]) for i in range(len(word))]
            if center_position not in word_positions:
                raise NoCenterLetterException("No hay letra en el centro")
            self.put_word(word, location, orientation)
            self.first_time = False
            return True  
        
    def get_word_cells(self, word, location, orientation):
        word_cells = [] 
        row, col = location 

        for letter in word:
            word_cells.append(self.grid[row][col])  
            if orientation.upper() == 'H':
                col += 1  
            else:
                row += 1  

        return word_cells
        
    def put_word(self, word_list_of_tiles, location, orientation):
        self.validate_word_inside_board(word_list_of_tiles, location, orientation)
        len_word = len(word_list_of_tiles)
        row, col = location
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
        for i in range(len_word):
            if self.grid[row][col].tile is None:
                self.grid[row][col].tile = word_list_of_tiles[i]
            row += row_increment
            col += col_increment

    def validate_word_connected(self, word, location, orientation):
        r, c = location
        count = 0
        for letter in word:
            if 0 <= r < 15 and 0 <= c < 15 and self.grid[r][c].tile is not None:
                count += 1
            if orientation == 'H':
                c += 1
            elif orientation == 'V':
                r += 1
        if count != 0:
            return True
        else:
            raise NoWordConnectedException('La palabra tiene que estar conectada')
                    
    def validate_crossing_words(self, word, location, orientation):
            row, col = location    
            if not word_in_dictionary(word):
                return False   
            for i, letter in enumerate(word):
                cross_row, cross_col = (row, col + i) if orientation == 'H' else (row + i, col)

                if self.grid[cross_row][cross_col].tile:
                    existing_tile = self.grid[cross_row][cross_col].tile                
                    if existing_tile.letter != letter:
                        return True
            return False
            
    def get_word_without_intersections(self,word,location,orientation):
        result = ''
        for i in range(len(word)):
            cell = self.grid[location[0] + (i if not orientation else 0)][location[1] + (i if orientation else 0)].tile
            if not cell:
                result += word[i]
        return result
    
    def word_to_cells(self, word, row, column, orientation):
        list_tiles = self.convert_word_to_tiles(word)
        list_cell = []
        for i in range(len(word)):
            tile = list_tiles[i]
            cell_row = row
            cell_column = column
            cell = copy.copy(self.grid[cell_row][cell_column])
            cell.add_letter(tile, cell_row, cell_column)
            list_cell.append(cell)
            if orientation == 'H':
                column += 1  
            elif orientation == 'V':
                row += 1  
        return list_cell

    def display_board(self):
        print("Tablero de Scrabble:")
        print("     0     1     2     3     4     5     6     7     8     9    10    11    12    13    14  ")

        for row in range(15):
            row_str = str(row)
            row_str = row_str.rjust(2)
            print(row_str, end = ' ')
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

        if cell.tile is not None:
            print(f"[ {cell.tile.letter} ]", end=' ')
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