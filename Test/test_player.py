import unittest
from game.player import Player
from game.models import Tile

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
    
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
        result = player.play_word(word_to_play)
        
        self.assertFalse(result)
        self.assertEqual(len(player.tiles), 3)

if __name__ == '__main__':
    unittest.main()