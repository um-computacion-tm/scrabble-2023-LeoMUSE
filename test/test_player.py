import unittest
from game.player import Player
from game.tile import Tile
from io import StringIO
import sys

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(len(player_1.tiles), 0)
    
    def test_play_word_valid(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        
        word_to_play = [player.tiles[0], player.tiles[1]]
        result = player.play_word(word_to_play)

        self.assertTrue(result)
        self.assertEqual(len(player.tiles), 1)

    def test_play_word_invalid(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('D', 2), Tile('C', 3)]

        word_to_play = [Tile('A', 1), Tile('D', 2)]
        with self.assertRaises(ValueError):
            player.play_word(word_to_play)
        
        self.assertEqual(len(player.tiles), 3)

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

if __name__ == '__main__':
    unittest.main()