import unittest

from unittest.mock import patch, call
from game.scrabbleCli import ScrabbleCli, NoLettersExeption, NoCenterLetterException, NoValidWordException
from game.scrabble import ScrabbleGame, NoValidWordException
from game.player import Player
from game.tile import Tile
from game.board import Board
from game.bagtile import BagTiles
from io import StringIO

class TestScrabbleCli(unittest.TestCase):

    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        scrabble_cli = ScrabbleCli(player_count=3)
        self.assertEqual(scrabble_cli.get_player_count(), 3)

    @patch('builtins.input', side_effect=['A', '3'])
    @patch('builtins.print')
    def test_get_player_count_wrong_input(self, input_patched, mock_print):
        scrabble_cli = ScrabbleCli(player_count=3)
        self.assertEqual(scrabble_cli.get_player_count(),3)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['10', '2'])
    def test_get_player_count_control_max(self, input_patched, mock_print):
        scrabble_cli = ScrabbleCli(player_count=1)
        self.assertEqual(scrabble_cli.get_player_count(),2)

    @patch('builtins.print')
    @patch('builtins.input', side_effect = ['S'])
    def test_quit_game(self, mock_input, mock_print):
            scrabble_cli = ScrabbleCli(player_count=2)
            self.assertFalse(scrabble_cli.quit_game)
            scrabble_cli.quit()
            self.assertTrue(scrabble_cli.quit_game)

    def test_play_joker(self):
            scrabble_cli = ScrabbleCli(player_count=2)
            scrabble_cli.quit_game = False
            scrabble_cli.game.players[0].tiles = [Tile(letter=' ', value=0), Tile(letter='A', value=1)]
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                with patch("builtins.input", return_value='B'):
                    scrabble_cli.play_joker()
            self.assertEqual(scrabble_cli.game.players[0].tiles[0].letter, 'B')

    @patch('builtins.input', side_effect=['S'])
    @patch('builtins.print')
    def test_skip_turn(self, mock_input, mock_print):
        scrabble_cli = ScrabbleCli(player_count=1)
        result = scrabble_cli.skip_turn()
        self.assertEqual(result, None)  

    @patch('builtins.input', side_effect=['N']) 
    def test_do_not_skip_turn(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=1)
        result = scrabble_cli.skip_turn()
        self.assertEqual(result, "Ingrese una Palabra.")
    
    def test_draw_tiles_first_time(self):
        game = ScrabbleGame(players_count=2) 
        cli = ScrabbleCli(player_count=2)
        cli.game = game  
        player1 = game.players[0]
        player1.tiles.extend([])  
        player2 = game.players[1]
        player2.tiles.extend([])
        cli.draw_tiles()
        self.assertEqual(len(player1.tiles), 7)
        self.assertEqual(len(player2.tiles), 7)

    def test_draw_tiles(self):
        game = ScrabbleGame(players_count=2)  
        cli = ScrabbleCli(player_count=2)
        cli.game = game  
        player = game.players[0]
        player.tiles.extend(["A", "B", "C"]) 
        cli.draw_tiles()
        self.assertEqual(len(player.tiles), 7)

    def test_show_tiles(self):
        scrabble_cli = ScrabbleCli(player_count=0)
        player = Player()  
        example_tiles = [('A', 1), ('B', 3), ('C', 3), ('D', 2)]
        player.tiles = example_tiles
        scrabble_cli.game.current_player = 0 
        scrabble_cli.game.players.append(player)
        with unittest.mock.patch('sys.stdout', new_callable= StringIO) as mock_stdout:
            scrabble_cli.show_tiles(player)
            printed_output = mock_stdout.getvalue()
        expected_output = "Fichas: [('A', 1), ('B', 3), ('C', 3), ('D', 2)] del jugador 0\n"
        self.assertEqual(printed_output, expected_output)

    @patch('builtins.print')
    @patch.object(ScrabbleCli, "get_player_count")
    @patch.object(ScrabbleCli, "draw_tiles")
    @patch.object(ScrabbleCli, "show_tiles")
    @patch.object(ScrabbleCli, "show_board")
    @patch.object(ScrabbleCli, "player_turn")
    @patch.object(ScrabbleGame, "is_game_over")
    def test_start_game(self, mock_print, mock_get_player_count, mock_draw_tiles, mock_show_tiles, mock_show_board, mock_player_turn, mock_is_game_over):
        mock_is_game_over.return_value = True
        scrabble_cli = ScrabbleCli(player_count=2)
        scrabble_cli.start_game()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1'])
    def test_player_turn_play(self, mock_input, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        with self.assertRaises(StopIteration):
            scrabble_cli.player_turn()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2'])
    def test_player_turn_skip(self, mock_input, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        with self.assertRaises(StopIteration):
            scrabble_cli.player_turn()

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3'])
    def test_player_turn_scores(self, mock_input, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        with self.assertRaises(StopIteration):
            scrabble_cli.player_turn()

    @patch('builtins.print')
    def test_show_board(self, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        scrabble_cli.show_board()

    @patch('builtins.print')
    def test_show_scores(self, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        scrabble_cli.show_scores()
        mock_print.assert_called()

    @patch('builtins.input', side_effect=[ 'CASA', '7', '7', 'H'])
    def test_get_word_location_orientation(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=2)
        word, location, orientation = scrabble_cli.get_word_location_orientation()
        self.assertEqual(word, 'CASA')
        self.assertEqual(location, (7,7))
        self.assertEqual(orientation, 'H')

    @patch('builtins.input', side_effect=[ '0'])
    def test_get_word_location_orientation_return(self, mock_input):
        scrabble_cli = ScrabbleCli(player_count=2)
        word, location, orientation = scrabble_cli.get_word_location_orientation()
        self.assertEqual(word, '0')
        self.assertEqual(location, None)
        self.assertEqual(orientation, None)

    @patch('builtins.print')
    def test_exchange_invalid_format(self, mock_print):
        game = ScrabbleGame(players_count = 2)
        scrabble_cli = ScrabbleCli(player_count = 2)
        current_player = game.players[game.current_player]
        current_player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1), Tile('F', 4), Tile('G', 2)]
        with patch('builtins.input', side_effect=['ABC', '0']):
            scrabble_cli.exchange()
        self.assertEqual(len(current_player.tiles), 7)
        self.assertIn('A', [tile.letter for tile in current_player.tiles])
        self.assertIn('B', [tile.letter for tile in current_player.tiles])
        self.assertIn('C', [tile.letter for tile in current_player.tiles])

    @patch('builtins.print')
    def test_exchange_invalid_indices(self, mock_print):
        game = ScrabbleGame(players_count = 2)
        scrabble_cli = ScrabbleCli(player_count = 2)
        current_player = game.players[game.current_player]
        current_player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1), Tile('F', 4), Tile('G', 2)]
        with patch('builtins.input', side_effect=['1234567', '0']):
            scrabble_cli.exchange()
        self.assertEqual(len(current_player.tiles), 7)
        self.assertIn('A', [tile.letter for tile in current_player.tiles])
        self.assertIn('B', [tile.letter for tile in current_player.tiles])
        self.assertIn('C', [tile.letter for tile in current_player.tiles])

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '1 2 3 4', '0'])
    def test_exchange_tiles(self, mock_input, mock_print):
        scrabble_cli = ScrabbleCli(player_count=2)
        player = scrabble_cli.game.players[0]
        player.tiles = [Tile('H', 4), Tile('O', 1), Tile('L', 1), Tile('A', 1)]
        scrabble_cli.exchange()
        self.assertEqual(len(player.tiles), 4)

    @patch('builtins.input', side_effect=['CASA', '7', '7', 'H'])
    @patch.object(ScrabbleGame, 'correct_word')
    @patch.object(ScrabbleGame, 'play_word') 
    @patch('builtins.print')
    def test_place_and_put_word(self, mock_input, mock_print, mock_correct_word, mock_play_word):
        your_instance = ScrabbleCli(player_count=2)
        your_instance.first_time = True
        result = your_instance.place_and_put_word()
        self.assertEqual(result, 'terminar')

    @patch('builtins.input', side_effect=['CASA', '7', '8', 'H'])
    @patch.object(ScrabbleGame, 'correct_word')
    @patch.object(ScrabbleGame, 'play_word') 
    @patch('builtins.print')
    def test_place_and_put_word_not_first_time(self, mock_input, mock_print, mock_correct_word, mock_play_word):
        your_instance = ScrabbleCli(player_count=2)
        your_instance.first_time = False
        result = your_instance.place_and_put_word()
        self.assertEqual(result, 'terminar')

    @patch('builtins.input', side_effect=['0'])
    @patch('builtins.print')
    def test_place_and_put_word_quit(self, mock_input, mock_print):
        your_instance = ScrabbleCli(player_count=2)
        result = your_instance.place_and_put_word()
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()