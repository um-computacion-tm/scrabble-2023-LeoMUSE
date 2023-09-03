import unittest
from game.tile import Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)

if __name__ == '__main__':
    unittest.main()