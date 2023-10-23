import unittest
from game.scrabble import ScrabbleGame
from game.player import Player
from game.bagtile import BagTiles
from game.tile import Tile
from game.board import Board
from game.cell import Cell
import io
import sys

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(len(scrabble_game.players),3)
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_start_game(self):
        player = Player()
        game = ScrabbleGame(players_count = 3)
        game.start_game()

        for player in game.players:
            self.assertEqual(len(player.tiles), 7)

    def test_next_turn(self):
        game = ScrabbleGame(players_count=3)
        self.assertEqual(game.current_player, 0)
        game.next_turn()
        self.assertEqual(game.current_player, 1)
        game.next_turn()
        self.assertEqual(game.current_player, 2)
        game.next_turn()
        self.assertEqual(game.current_player, 0)
        game.next_turn()
        self.assertEqual(game.current_player, 1)

    def test_set_time(self):
        game = ScrabbleGame(players_count = 2)
        game.set_time_limit(60)
        self.assertEqual(game.turn_limit, 60)

    def test_start_timer(self):
        game = ScrabbleGame(players_count = 2)
        game.set_time_limit(5)
        game.start_timer()
        import time
        time.sleep(6)
        self.assertEqual(game.current_player, 1)

    def test_pass_turn_scrabble(self):
        game = ScrabbleGame(players_count = 2)
        self.assertEqual(game.current_player, 0)
        game.pass_turn_scrabble(game.current_player)
        self.assertEqual(game.current_player, 1)
        game.pass_turn_scrabble(game.current_player)
        self.assertEqual(game.current_player, 0)

    def test_get_current_player(self):
        player1 = Player()
        player2 = Player()
        game = ScrabbleGame(players_count=2)
        game.players = [player1, player2]
        game.current_player = 0
        current_player = game.get_current_player()
        self.assertEqual(current_player, player1)
        game.current_player = 1
        current_player = game.get_current_player()
        self.assertEqual(current_player, player2)

    def test_is_game_over_with_tiles_in_bag(self):
        game = ScrabbleGame(players_count=2)
        self.assertFalse(game.is_game_over())

    def test_is_game_over_with_empty_bag(self):
        game = ScrabbleGame(players_count=2)
        game.bag_tiles.tiles = []
        self.assertTrue(game.is_game_over())

    def test_can_exchange_tiles_with_exchangeable_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('', 0)]
        game = ScrabbleGame(players_count=2)
        game.players = [player]
        game.current_player = 0
        self.assertTrue(game.can_exchange_tiles())

    def test_can_exchange_tiles_with_no_exchangeable_tiles(self):
        player = Player()
        player.tiles = [Tile('', 0)]
        game = ScrabbleGame(players_count=2)
        game.players = [player]
        game.current_player = 0
        self.assertFalse(game.can_exchange_tiles())

    def test_display_tiles(self):
        player = Player()
        scrabble = ScrabbleGame(players_count=3) 
        player.tiles = [
            Tile('B', 2),
            Tile('C', 3),
            Tile('D', 3),
            Tile('E', 1),
            Tile('F', 4),
            Tile('G', 2),
            Tile('H', 4),
        ]

        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabble.display_rack(player)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """[B,2] [C,3] [D,3] [E,1] [F,4] [G,2] [H,4] """
        self.assertEqual(output, expected_output)

    def test_validate_word_player_tiles_insufficient(self):
        game = ScrabbleGame(players_count = 3)
        game.players[0].tiles = []
        word = [Tile('A', 1)]
        location = (7, 7)
        orientation = "H"
        with self.assertRaises(ValueError):
            game.validate_word(word, location, orientation)

if __name__ == '__main__':
    unittest.main()