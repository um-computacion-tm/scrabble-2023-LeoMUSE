import unittest

from game.bagtile import BagTiles
from game.tile import Tile
from game.player import Player

from unittest.mock import patch

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles), 103)
        self.assertEqual(patch_shuffle.call_count, 1)
        self.assertEqual(patch_shuffle.call_args[0][0], bag.tiles)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(tiles), 2)
        self.assertEqual(len(bag.tiles), 103 - 2)

    def test_take_invalid(self):
        bag = BagTiles()
        with self.assertRaises(ValueError):
            tiles = bag.take(105)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles),105,)

    def test_tiles_in_bag(self):
        bag = BagTiles()
        bag.tiles = ['A', 'B', 'C', 'D', 'E']
        self.assertEqual(bag.tiles_in_bag(), 5)

if __name__ == '__main__':
    unittest.main()