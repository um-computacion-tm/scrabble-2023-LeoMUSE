import unittest
from game.player import Player, InsufficientTilesInHand
from game.tile import Tile
from io import StringIO
import sys

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 0)
    
    def test_has_letters_true(self):
        player = Player()
        player.tiles = [Tile('H', 2), Tile('E', 1), Tile('L', 1), Tile('O', 1)]
        word = [Tile('H', 2), Tile('E', 1), Tile('L', 1), Tile('O', 1)]
        result = player.validate_tiles_in_word(word)
        self.assertTrue(result)
    
    def test_validate_tiles_in_word_invalid(self):
        player = Player()
        player.tiles = [Tile('H', 2), Tile('E', 1), Tile('L', 3), Tile('O', 1)]
        tiles_to_validate = [Tile('H', 1), Tile('E', 1), Tile('L', 1), Tile('L', 1), Tile('O', 1)]
        result = player.validate_tiles_in_word(tiles_to_validate)
        self.assertFalse(result)

    def test_assign_wildcard_value(self):
        player = Player()
        player.tiles = [Tile('', 0), Tile('A', 1), Tile('B', 1)]

        letter = 'C'
        value = 2

        result = player.assign_wildcard_value(letter, value)
        self.assertTrue(result)
        self.assertEqual(len(player.tiles), 3)
        self.assertEqual(player.tiles[2].letter, 'C')
        self.assertEqual(player.tiles[2].value, 2)
    
    def test_wildcard_whit_no_wildcard(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3)]

        letter = 'C'
        value = 2

        player.assign_wildcard_value(letter, value)
        self.assertEqual(len(player.tiles), 2)

    def test_pass_turn(self):
        player = Player()
        self.assertFalse(player.passed_turn)
        player.pass_turn_player()
        self.assertTrue(player.passed_turn)

    def test_get_score(self):
        player = Player()
        player.score = 42
        self.assertEqual(player.get_score(), 42)

    def test_get_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        tiles = player.get_tiles()
        expected_tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        self.assertEqual(
            [(tile.letter, tile.value) for tile in tiles],
            [(tile.letter, tile.value) for tile in expected_tiles]
        )


if __name__ == '__main__':
    unittest.main()