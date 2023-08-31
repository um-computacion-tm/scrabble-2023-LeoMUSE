import unittest
from game.scrabble import ScrabbleGame
from game.player import Player
from game.bagtile import BagTiles

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_start_game(self):
        player = Player()
        game = ScrabbleGame(players_count=2)
        game.start_game()

        for player in game.players:
            self.assertEqual(len(player.tiles), 7)

if __name__ == '__main__':
    unittest.main()