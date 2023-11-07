import unittest
from game.player import Player, InsufficientTilesInHand
from game.tile import Tile
from io import StringIO
from game.bagtile import BagTiles

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player = Player()
        self.assertEqual(len(player.tiles), 0)
        self.assertFalse(player.passed_turn)
        self.assertEqual(player.score, 0)

    def test_player_has_letter(self):
        bagperson = BagTiles()
        p = Player()
        bagperson.tiles = [
            Tile(letter='P', value=3),
            Tile(letter='E', value=1),
            Tile(letter='R', value=1),
            Tile(letter='R', value=1),
            Tile(letter='O', value=1),
            Tile(letter='E', value=1),
            Tile(letter='G', value=2),
        ]
        p.tiles = bagperson.tiles
        self.assertTrue(p.validate_tiles_in_word('PERRO', p.tiles))

    def test_player_has_no_letter(self):
        bagperson = BagTiles()
        p = Player()
        bagperson.tiles = [
                Tile(letter='P', value=3),
                Tile(letter='E', value=1),
                Tile(letter='R', value=1),
                Tile(letter='R', value=1),
                Tile(letter='O', value=1),
                Tile(letter='E', value=1),
                Tile(letter='G', value=2),
            ]
        p.tiles = bagperson.tiles
        self.assertFalse(p.validate_tiles_in_word('perrx', p.tiles))
            
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

    def test_play_valid_word(self):
            player = Player()
            player.tiles = [
                Tile(letter='H', value=4),
                Tile(letter='O', value=1),
                Tile(letter='L', value=1),
                Tile(letter='A', value=1),
                Tile(letter='C', value=3),
                Tile(letter='U', value=1),
                Tile(letter='M', value=3),
            ]
            word = 'HOLA'
            result = player.remove_letters(word)
            self.assertTrue(result)
            self.assertEqual(len(player.tiles), 3)

    def test_pass_turn_player(self):
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
        tiles = player.show_tiles()
        expected_tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        self.assertEqual(
            [(tile.letter, tile.value) for tile in tiles],
            [(tile.letter, tile.value) for tile in expected_tiles]
        )

    def test_add_score(self):
        player = Player()
        player.add_score(10)

        self.assertEqual(player.score, 10)

if __name__ == '__main__':
    unittest.main()