import unittest
from game.board import Board
from game.cell import Cell
from game.tile import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[0]),15,)

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=1,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=True)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        cell1 = Cell(multiplier=3,multiplier_type=True)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        cell1 = Cell(multiplier=3,multiplier_type=True,active=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=False,active=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type=True,active=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=False,active=False)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 5)
    
    def test_word_inside_board_H(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)
    
    def test_word_inside_board_V(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_word_out_of_board_H(self):
        board = Board()
        word = "Facultad"
        location = (1, 14)
        orientation = "H"
        
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)

    def test_word_out_of_board_V(self):
        board = Board()
        word = "Facultad"
        location = (14, 1)
        orientation = "V"
        
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertFalse(word_is_valid)

if __name__ == '__main__':
    unittest.main()
