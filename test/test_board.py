import unittest
from game.board import Board, NoWordConnectedException, NoValidCrossWordException, NoCenterLetterException
from game.cell import Cell
from game.tile import Tile
from game.player import Player
from game.scrabble import ScrabbleGame
from game.board import TL,TW,DW,DL
import io

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[0]),15,)

class TestCalculateWordValue(unittest.TestCase):

    def test_board_cell_2_6(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[2][6].multiplier,'letter' )
        self.assertEqual(cell[2][6].multiplier_type, 2 )

    def test_simple(self):
        cell1 = Cell(multiplier=1,multiplier_type=False)
        cell1.add_letter(Tile('C', 1), row=7, col=7) 
        cell2 = Cell(multiplier=1,multiplier_type=False)
        cell2.add_letter(Tile('A', 1), row=7, col=8)
        cell3 = Cell(multiplier=1,multiplier_type=False)
        cell3.add_letter(Tile('S', 2), row=7, col=9)
        cell4 = Cell(multiplier=1,multiplier_type=False)
        cell4.add_letter(Tile('A', 1), row=8, col=10)

        location = (7,7)
        orientation = 'H'
        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word, location, orientation)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        cell1 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell1.add_letter(Tile('C', 1), row=7, col=7) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell2.add_letter(Tile('A', 1), row=7, col=8)
        cell3 = Cell(multiplier=2,multiplier_type="letter",active=True)
        cell3.add_letter(Tile('S', 2), row=7, col=9)
        cell4 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell4.add_letter(Tile('A', 1), row=7, col=10)

        location = (7,7)
        orientation = 'H'
        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word, location, orientation)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        cell1 = Cell(multiplier=2,multiplier_type="word", active=True)
        cell1.add_letter(Tile('C', 1), row=7, col=7) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell2.add_letter(Tile('A', 1), row=7, col=8)
        cell3 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell3.add_letter(Tile('S', 2), row=7, col=9)
        cell4 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell4.add_letter(Tile('A', 1), row=7, col=10)

        location = (7,7)
        orientation = 'H'
        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word,location,orientation)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        cell1 = Cell(multiplier=3,multiplier_type="word",active=True)
        cell1.add_letter(Tile('C', 1), row=7, col=7) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell2.add_letter(Tile('A', 1), row=7, col=8)
        cell3 = Cell(multiplier=2,multiplier_type="letter",active=True)
        cell3.add_letter(Tile('S', 2), row=7, col=9)
        cell4 = Cell(multiplier=1,multiplier_type=None,active=True)
        cell4.add_letter(Tile('A', 1), row=7, col=10)

        location = (7,7)
        orientation = 'H'
        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word, location, orientation)
        self.assertEqual(value, 21)

    def test_with_letter_word_multiplier_no_active(self):
        cell1 = Cell(multiplier=3,multiplier_type="word",active=False)
        cell1.add_letter(Tile('C', 1), row=7, col=7) 
        cell2 = Cell(multiplier=1,multiplier_type=None,active=False)
        cell2.add_letter(Tile('A', 1), row=7, col=8)
        cell3 = Cell(multiplier=2,multiplier_type="word",active=False)
        cell3.add_letter(Tile('S', 2), row=7, col=9)
        cell4 = Cell(multiplier=1,multiplier_type=None,active=False)
        cell4.add_letter(Tile('A', 1), row=7, col=10)

        location = (7,7)
        orientation = 'H'
        word = [cell1, cell2, cell3, cell4]
        value = Board().calculate_word_value(word, location, orientation)
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
        board.grid[7][7].add_letter(Tile('C', 1),row=7,col=7)
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
        board.grid[7][7].add_letter(Tile("C", 1), row=7, col=7)
        board.grid[8][7].add_letter(Tile("A", 1), row=8, col=7)
        board.grid[9][7].add_letter(Tile("S", 1), row=9, col=7)
        board.grid[10][7].add_letter(Tile("A", 1), row=10, col=7)
        word = "Facultad"
        location = (4, 7)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        self.assertTrue(word_is_valid)
    
    def test_put_words_horizontal(self):
            board = Board()
            tile1 = Tile('H',4)
            tile2 = Tile('O',1)
            tile3 = Tile('Y',4)
            word = [tile1, tile2, tile3]
            board.put_word(word, (4,4),'H')
            self.assertEqual(board.grid[4][4].tile, tile1) #para que 'H' sea igual a 'H'
            self.assertEqual(board.grid[4][5].tile, tile2)
            self.assertEqual(board.grid[4][6].tile, tile3)

    def test_put_words_vertical(self):
            board = Board()
            tile1 = Tile('H',4)
            tile2 = Tile('O',1)
            tile3 = Tile('Y',4)
            word = [tile1, tile2, tile3]
            board.put_word(word, [4,4],'V')
            self.assertEqual(board.grid[4][4].tile, tile1) #para que 'H' sea igual a 'H'
            self.assertEqual(board.grid[5][4].tile, tile2)
            self.assertEqual(board.grid[6][4].tile, tile3)

    def test_validate_crossing_words(self):
        board=Board()
        board.grid[7][7].tile = Tile('C',1)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',2)
        board.grid[7][10].tile = Tile('A',1)
        board.grid[6][8].tile = Tile('L',1)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[8][8].tile = Tile('Z',1)
        board.grid[9][8].tile = Tile('O',1)
        word1 = 'lazo'
        location1 = (6,8)
        orientation1 = 'V'
        self.assertEqual(board.validate_crossing_words(word1,location1,orientation1),True)

    def test_validate_crossing_words_false(self):
        board=Board()
        board.grid[7][7].tile = Tile('C',1)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',2)
        board.grid[7][10].tile = Tile('A',1)
        word1 = 'faca'
        location1 = (5,8)
        orientation1 = 'H'
        self.assertEqual(board.validate_crossing_words(word1,location1,orientation1),False)

    def test_display_board_with_all_multipliers(self):
        board = Board()

        expected_output = [
            "Tablero de Scrabble:",
            "     0     1     2     3     4     5     6     7     8     9    10    11    12    13    14  ",
            " 0 [W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
            " 1 [   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            " 2 [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            " 3 [L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            " 4 [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            " 5 [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            " 6 [   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            " 7 [W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [   ] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
            " 8 [   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            " 9 [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            "10 [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            "11 [L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            "12 [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            "13 [   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            "14 [W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
        ]

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board.display_board()
            output = mock_stdout.getvalue()

        cleaned_output = [line.strip() for line in output.strip().split('\n')]
        cleaned_expected_output = [line.strip() for line in expected_output]
        self.maxDiff = None
        self.assertEqual(cleaned_output, cleaned_expected_output)

    def test_display_board_with_all_multipliers_and_word(self):
        board = Board()
        word1 = [Tile('C', 1), Tile('A', 1), Tile('S', 2), Tile('A', 1)]
        location1 = (7,7)
        orientation1 = 'H'

        word2 = [Tile('C', 1), Tile('A', 1), Tile('S', 2), Tile('A', 1)]
        location2 = (7,7)
        orientation2 = 'V'

        board.put_word(word1, location1, orientation1)
        board.put_word(word2, location2, orientation2)

        expected_output = [
            "Tablero de Scrabble:",
            "  0     1     2     3     4     5     6     7     8     9    10    11    12    13    14  ",
            " 0 [W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
            " 1 [   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            " 2 [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            " 3 [L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            " 4 [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            " 5 [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            " 6 [   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            " 7 [W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [ C ] [ A ] [ S ] [ A ] [L,2] [   ] [   ] [W,3]",
            " 8 [   ] [   ] [L,2] [   ] [   ] [   ] [L,2] [ A ] [L,2] [   ] [   ] [   ] [L,2] [   ] [   ]",
            " 9 [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [ S ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ]",
            "10 [   ] [   ] [   ] [   ] [W,2] [   ] [   ] [ A ] [   ] [   ] [W,2] [   ] [   ] [   ] [   ]",
            "11 [L,2] [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ] [L,2]",
            "12 [   ] [   ] [W,2] [   ] [   ] [   ] [L,2] [   ] [L,2] [   ] [   ] [   ] [W,2] [   ] [   ]",
            "13 [   ] [W,2] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [L,3] [   ] [   ] [   ] [W,2] [   ]",
            "14 [W,3] [   ] [   ] [L,2] [   ] [   ] [   ] [W,3] [   ] [   ] [   ] [L,2] [   ] [   ] [W,3]",
        ]

        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            board.display_board()
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
        location = (3, 3)
        orientation = "H"
        with self.assertRaises(NoCenterLetterException):
            board.put_word_first_time(word, location, orientation)
    
    def test_word_to_cells_horizontal(self):
        board = Board()
        word = "SANDIA"
        row = 7
        column = 7
        orientation = "H"
        result = board.word_to_cells(word, row, column, orientation)
        self.assertEqual(len(result), len(word))

    def test_word_to_cells_vertical(self):
        board = Board()
        word = "SANDIA"
        row = 7
        column = 7
        orientation = "V"
        result = board.word_to_cells(word, row, column, orientation)
        self.assertEqual(len(result), len(word))

    def test_get_word_without_intersection(self):
        board=Board()
        board.grid[7][7].tile = Tile('C',1)
        board.grid[7][8].tile = Tile('A',1)
        board.grid[7][9].tile = Tile('S',2)
        board.grid[7][10].tile = Tile('A',1)
        word = 'MASA'
        location = (6,8)
        orientation = False
        self.assertEqual(board.get_word_without_intersections(word,location,orientation),'MSA')

    def test_validate_word_connected_with_disconnected_word(self):
        board = Board()
        word = "PALABRA"
        location = (7, 7)
        orientation = 'H'

        with self.assertRaises(NoWordConnectedException):
            board.validate_word_connected(word, location, orientation)

    def test_get_word_cells_horizontal(self):
        # Configurar el juego y el tablero de prueba
        game = ScrabbleGame(players_count=2)
        game.board.grid = [
            [Tile('A', 1), Tile('B', 3), Tile('C', 3)],
            [Tile('D', 2), Tile('E', 1), Tile('F', 4)],
            [Tile('G', 2), Tile('H', 3), Tile('I', 2)]
        ]

        # Definir la palabra, ubicación y orientación
        word = "ABC"
        location = (0, 0)
        orientation = "H"

        # Llamar al método get_word_cells
        word_cells = game.board.get_word_cells(word, location, orientation)

        # Verificar si las celdas devueltas coinciden con la palabra
        expected_cells = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        self.assertEqual(word_cells, expected_cells)

    def test_get_word_cells_vertical(self):
        # Configurar el juego y el tablero de prueba
        game = ScrabbleGame(players_count=2)
        game.board.grid = [
            [Tile('A', 1), Tile('B', 3), Tile('C', 3)],
            [Tile('D', 2), Tile('E', 1), Tile('F', 4)],
            [Tile('G', 2), Tile('H', 3), Tile('I', 2)]
        ]

        # Definir la palabra, ubicación y orientación
        word = "ADG"
        location = (0, 0)
        orientation = "V"

        # Llamar al método get_word_cells
        word_cells = game.board.get_word_cells(word, location, orientation)

        # Verificar si las celdas devueltas coinciden con la palabra
        expected_cells = [Tile('A', 1), Tile('D', 2), Tile('G', 2)]
        self.assertEqual(word_cells, expected_cells)

if __name__ == '__main__':
    unittest.main()
