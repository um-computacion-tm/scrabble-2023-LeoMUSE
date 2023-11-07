import unittest
from game.tile import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)

    def test_tile_equality(self):
        tile1 = Tile('A', 1)
        tile2 = Tile('A', 1)
        tile3 = Tile('B', 3)

        self.assertTrue(tile1 == tile2)
        self.assertFalse(tile1 == tile3)
        self.assertFalse(tile1 == "A")

if __name__ == '__main__':
    unittest.main()