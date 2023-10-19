import unittest
from game.board import Board
from game.cell import Cell
from game.tile import Tile
from game.player import Player
from game.board import TL,TW,DW,DL
import io

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
        cell1 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type="letter",active=True)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell1 = Cell(multiplier=2,multiplier_type="word", active=True)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        cell1 = Cell(multiplier=3,multiplier_type="word",active=True)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type="letter",active=True)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell4.add_letter(Tile('A', 1))

        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word)
        self.assertEqual(value, 21)

    def test_with_letter_word_multiplier_no_active(self):
        cell1 = Cell(multiplier=3,multiplier_type="word",active=False)
        cell1.add_letter(Tile('C', 1)) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=False)
        cell2.add_letter(Tile('A', 1))
        cell3 = Cell(multiplier=2,multiplier_type="word",active=False)
        cell3.add_letter(Tile('S', 2))
        cell4 = Cell(multiplier=1,multiplier_type=None,active=False)
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
        
        with self.assertRaises(ValueError):
            board.validate_word_inside_board(word, location, orientation)

    def test_word_out_of_board_V(self):
        board = Board()
        word = "Facultad"
        location = (14, 1)
        orientation = "V"
        
        with self.assertRaises(ValueError):
            board.validate_word_inside_board(word, location, orientation)

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        assert board.is_empty == False      

    def test_place_word_empty_board_H_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_place_word_empty_board_H_worng(self):
        board = Board()
        word = "Facultad"
        location = (1, 14)
        orientation = "H"

        with self.assertRaises(ValueError):
            board.validate_word_inside_board(word, location, orientation)

    def test_place_word_empty_board_V_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "V"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)

    def test_place_word_empty_board_V_wrong(self):
        board = Board()
        word = "Facultad"
        location = (14, 1)
        orientation = "V"

        with self.assertRaises(ValueError):
            board.validate_word_inside_board(word, location, orientation)

    def test_place_word_not_empty_board_H_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile("C", 1))
        board.grid[8][7].add_letter(Tile("A", 1))
        board.grid[9][7].add_letter(Tile("S", 1))
        board.grid[10][7].add_letter(Tile("A", 1))
        word = "Facultad"
        location = (4, 7)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)
    
    def test_put_word_horizontal(self):
        board = Board()
        word = 'HELLO'
        location = (7, 7)
        orientation = 'H'

        board.put_word(word, location, orientation)

        for i, letter in enumerate(word):
            self.assertEqual(board.grid[7][7 + i].letter, letter)

    def test_put_word_vertical(self):
        board = Board()
        word = 'VERTICAL'
        location = (7, 7)
        orientation = 'V'

        board.put_word(word, location, orientation)

        for i, letter in enumerate(word):
            self.assertEqual(board.grid[7 + i][7].letter, letter)

    def test_word_connected_horizontal(self):
        board = Board()
        word = "CASA"
        location = (7, 7) 
        orientation = "H"  

        board.grid[7][8].tile = "A"
        board.grid[7][9].tile = "S"
        board.grid[7][10].tile = "A"

        result = board.validate_word_connected(word, location, orientation)
        self.assertTrue(result)

    def test_word_connected_vertical(self):
        board = Board()
        word = "CASA"
        location = (7, 7)
        orientation = "V"

        board.grid[6][7].tile = "A"
        board.grid[5][7].tile = "S"
        board.grid[4][7].tile = "A"

        result = board.validate_word_connected(word, location, orientation)
        self.assertTrue(result)

    def test_word_not_connected(self):
        board = Board()
        word = "CASA"
        location = (7, 7)
        orientation = "H"

        with self.assertRaises(ValueError):
            board.validate_word_connected(word, location, orientation)

    def test_display_board_with_all_multipliers(self):
        board = Board()

        expected_output = [
            "Tablero de Scrabble:",
            "  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14  ",
            "[W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
            "[   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            "[   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            "[L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            "[   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            "[   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            "[   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            "[W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [   ] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
            "[   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            "[   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            "[   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            "[L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            "[   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            "[   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            "[W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
        ]

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board.display_board(board)
            output = mock_stdout.getvalue()

        cleaned_output = [line.strip() for line in output.strip().split('\n')]
        cleaned_expected_output = [line.strip() for line in expected_output]
        self.maxDiff = None
        self.assertEqual(cleaned_output, cleaned_expected_output)

    def test_display_board_with_all_multipliers_and_word(self):
        board = Board()
        player = Player()
        player.tiles = [Tile('H', 2), Tile('E', 1), Tile('L', 4), Tile('O', 1), Tile('O', 1)]
        word = [Tile('H', 2), Tile('E', 1), Tile('L', 4), Tile('L', 4), Tile('O', 1)]
        location = ( 7, 7 )
        orientation = "H"
        board.put_word(word, location, orientation)

        expected_output = [
            "Tablero de Scrabble:",
            "  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14  ",
            "[W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
            "[   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            "[   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            "[L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            "[   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            "[   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            "[   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            "[W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [ H ] [ E ] [ L ] [ L ] [ O ] [   ] [   ] [W,3]",
            "[   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            "[   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            "[   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            "[L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            "[   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            "[   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            "[W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
        ]

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board.display_board(board)
            output = mock_stdout.getvalue()

        cleaned_output = [line.strip() for line in output.strip().split('\n')]
        cleaned_expected_output = [line.strip() for line in expected_output]
        self.maxDiff = None
        self.assertEqual(cleaned_output, cleaned_expected_output)

    def test_put_word_first_time_horizontal(self):
        board = Board()
        word = "HELLO"
        location = (7, 7)
        orientation = "H"
        result = board.put_word_first_time(word, location, orientation)
        self.assertTrue(result)

    def test_put_word_first_time_vertical(self):
        board = Board()
        word = "WORLD"
        location = (7, 7)
        orientation = "V"
        result = board.put_word_first_time(word, location, orientation)
        self.assertTrue(result)

    def test_put_word_first_time_invalid(self):
        board = Board()
        word = "INVALID"
        location = (3, 3)  # Not the center
        orientation = "H"
        with self.assertRaises(ValueError):
            board.put_word_first_time(word, location, orientation)

if __name__ == '__main__':
    unittest.main()
