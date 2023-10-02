import unittest
from game.dictionary import Dictionary
from game.board import Board
from game.cell import Cell
from game.tile import Tile

class TestDictionary(unittest.TestCase):
    def test_dictionary_true(self):
        board = Board()
        dictionary = Dictionary()
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=1,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]

        file_path = dictionary.file_path
        self.assertEqual(board.check_word(word, file_path), True)

    def test_dictionary_false(self):
        board = Board()
        dictionary = Dictionary()
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('S', 2))
        cell3 = Cell(multiplier=1,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        
        file_path = dictionary.file_path
        self.assertEqual(board.check_word(word, file_path), False)

if __name__ == '__main__':
    unittest.main()