import unittest
from game.scrabble import ScrabbleGame, NoLettersExeption, NoValidWordException
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

    def test_is_game_over_true(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles = []
        self.assertTrue(scrabble_game.is_game_over())

    def test_is_game_over_false(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles = [Tile('A', 1)]
        self.assertFalse(scrabble_game.is_game_over())
        self.assertEqual(scrabble_game.game_state,'terminado')

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

    def test_give_player_tiles(self):
        game = ScrabbleGame(players_count=3)
        bag_tiles = game.bag_tiles

        initial_tile_count = bag_tiles.initial_tile_count
        self.assertEqual(bag_tiles.tiles_in_bag(), initial_tile_count)

        game.give_tiles(0, 7)

        self.assertEqual(len(game.players[0].tiles), 7)

        remaining_tiles = initial_tile_count - 7
        self.assertEqual(bag_tiles.tiles_in_bag(), remaining_tiles)

    
    def test_give_tiles(self):
        player = Player()
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.players = [player]
        scrabble_game.bag_tiles.tiles = [Tile('A', 1)] * 14
        
        scrabble_game.give_tiles(0, 7)
        
        self.assertEqual(len(player.tiles), 7)
        self.assertEqual(len(scrabble_game.bag_tiles.tiles), 14 - 7)

    def test_give_initial_tiles_to_all_players(self):
        player1 = Player()
        player2 = Player()
        player3 = Player()
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.players = [player1, player2, player3]
        scrabble_game.bag_tiles.tiles = [Tile('A', 1)] * 21
        
        scrabble_game.give_initial_tiles_to_all_players()

        self.assertEqual(len(player1.tiles), 7)
        self.assertEqual(len(player2.tiles), 7)
        self.assertEqual(len(player3.tiles), 7)

        self.assertEqual(len(scrabble_game.bag_tiles.tiles), 21 - 3 * 7)

    def test_give_initial_players_tiles(self):
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.give_initial_player_tiles(0)
        scrabble_game.give_initial_player_tiles(1)
        scrabble_game.give_initial_player_tiles(2)

        for player in scrabble_game.players:
            self.assertEqual(len(player.tiles), 7)

    def test_correct_word(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.board.grid[7][7].tile = Tile('C',1)
        scrabble_game.board.grid[7][8].tile = Tile('A',1)
        scrabble_game.board.grid[7][9].tile = Tile('S',1)
        scrabble_game.board.grid[7][10].tile = Tile('A',1)
        self.assertTrue(scrabble_game.correct_word('SACA', [6,8], 'V'))
        
    def test_correct_first_word_no_valid(self):
        scrabble_game = ScrabbleGame(players_count=3)
        with self.assertRaises(NoValidWordException):
            scrabble_game.put_on_the_board_first_time('WHO', [7,7], 'V')

    def test_put_first_time(self):
        scrabble_game = ScrabbleGame(players_count=3)
        tile1=Tile('H', 4)
        tile2= Tile('O', 1)
        tile3= Tile('L', 1)
        tile4 =Tile('A', 1)
        scrabble_game.players[scrabble_game.current_player].tiles=[tile1,tile2,tile3,tile4]
        scrabble_game.put_on_the_board_first_time('HOLA', (7,7), 'H')
        self.assertEqual(scrabble_game.board.grid[7][7].tile, Tile('H', 4))
        self.assertEqual(scrabble_game.board.grid[7][8].tile, Tile('O', 1))
        self.assertEqual(scrabble_game.board.grid[7][9].tile, Tile('L', 1))
        self.assertEqual(scrabble_game.board.grid[7][10].tile, Tile('A', 1))


    def test_get_tiles_on_board(self):
        game = ScrabbleGame(players_count=2)
        game.board.grid[7][7].tile = Tile('P', 1)
        game.board.grid[7][8].tile = Tile('A', 1)
        game.board.grid[7][9].tile = Tile('L', 1)
        game.board.grid[7][10].tile = Tile('A', 1)
        game.board.grid[7][11].tile = Tile('B', 1)
        game.board.grid[7][12].tile = Tile('R', 1)
        game.board.grid[7][13].tile = Tile('A', 1)

        word = 'PALABRA'
        location = (7, 7)
        orientation = 'H'
        tiles_on_board = game.get_tiles_on_board(word, location, orientation)
        expected_tiles = [Tile('P', 1), Tile('A', 1), Tile('L', 1), Tile('A', 1), Tile('B', 1), Tile('R', 1), Tile('A', 1)]
        self.assertEqual(tiles_on_board, expected_tiles)

    def test_play_word_valid(self):
        # Configurar el juego y los jugadores
        game = ScrabbleGame(players_count=2)
        player = game.players[game.current_player]
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]

        # Definir la palabra y la ubicación
        word = "CAB"
        location = (7, 7)
        orientation = "H"
        
        # Llamar al método play_word
        result = game.play_word(word, location, orientation, player.tiles)

        # Verificar si la jugada es válida
        self.assertTrue(result)

    def test_play_word_invalid(self):
        # Configurar el juego y los jugadores
        game = ScrabbleGame(players_count=2)
        player = game.players[game.current_player]
        player.tiles = [Tile('A', 1), Tile('B', 3)]

        # Definir la palabra y la ubicación
        word = "CAB"
        location = (7, 7)
        orientation = "H"
        
        # Llamar al método play_word
        with self.assertRaises(NoLettersExeption):
            game.play_word(word, location, orientation, player.tiles)

if __name__ == '__main__':
    unittest.main()