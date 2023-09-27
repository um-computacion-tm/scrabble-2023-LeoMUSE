import unittest
from game.scrabble import ScrabbleGame
from game.player import Player
from game.bagtile import BagTiles
from game.tile import Tile

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

if __name__ == '__main__':
    unittest.main()