import unittest
from game.scrabble import ScrabbleGame
from game.player import Player
from game.bagtile import BagTiles

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

if __name__ == '__main__':
    unittest.main()