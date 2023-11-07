import unittest
from game.cell import Cell
from game.tile import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=1, multiplier_type='')
        self.assertEqual(cell.multiplier,1)
        self.assertEqual(cell.multiplier_type,'')
        self.assertEqual(cell.active, True)
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='P', value=3)
        row = 7
        col = 7
        cell.add_letter(letter=letter, row=row, col=col)
        self.assertEqual(cell.letter, letter)

if __name__ == '__main__':
    unittest.main()