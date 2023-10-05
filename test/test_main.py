import unittest
from unittest.mock import patch, Mock
from io import StringIO
from game.main import get_player_count
from game.main import get_inputs
from game.main import main
from game.scrabble import ScrabbleGame
from game.board import Board
from game.tile import Tile
from game.cell import Cell
from game.player import Player

def mock_input(mock, inputs):
    for user_input in inputs:
        mock.write(f"{user_input}\n")
    mock.seek(0)

class TestMain(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        self.assertEqual(
            get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['A', '3'])
    def test_get_player_count_wrong_input(self, input_patched, print_patched):
        self.assertEqual(
            get_player_count(),
            3,
        )

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '1'])
    def test_get_player_count_control_max(self, input_patched, print_patched):
        self.assertEqual(
            get_player_count(),
            1,
        )

    @patch('builtins.print')
    @patch('game.main.show_player')
    @patch('game.main.show_board')
    @patch('game.main.get_player_count', return_value=3)
    @patch('game.main.get_inputs', return_value=((1, 3), 'H', 'CASA'))
    @patch.object(ScrabbleGame, 'is_game_over', side_effect=[True, False])
    @patch.object(ScrabbleGame, 'get_current_player', return_value=(0, "Player",))
    @patch.object(ScrabbleGame, 'play')
    def test_main(self, *args):
        main()

if __name__ == '__main__':
    unittest.main()
    