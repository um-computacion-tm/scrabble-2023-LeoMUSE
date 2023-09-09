import unittest
from unittest.mock import patch
from io import StringIO
from game.main import validate_number_of_players
from game.main import main

class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect = ["2"])

    def test_number_of_player_valid(self, mock_input):
        num_players = validate_number_of_players()
        self.assertEqual(num_players, 2)

    @patch('builtins.input', side_effect = ["0", "5", "3"])

    def test_number_of_player_not_valid_and_valid(self, mock_input):
        num_players = validate_number_of_players()
        self.assertEqual(num_players, 3)

    @patch('sys.stdout', new_callable = StringIO)
    @patch('builtins.input', side_effect = ["0", "5", "3"])
    def test_main(self, mock_input, mock_stdout):
        main()
        self.assertEqual(mock_input.call_count, 3)
        mock_stdout.seek(0)
        output = mock_stdout.read()
        self.assertIn("¡Bienvenido a Scrabble!", output)

if __name__ == '__main__':
    unittest.main