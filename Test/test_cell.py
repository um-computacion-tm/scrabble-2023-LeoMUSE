import unittest
from game.cell import Cell
from game.tile import Tile


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type=True)
        self.assertEqual(cell.multiplier,2)
        self.assertEqual(cell.multiplier_type,True)
        self.assertEqual(cell.active, True)
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type=False)
        letter = Tile(letter='P', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type=True)
        letter = Tile(letter='P', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type=False)
        letter = Tile(letter='P', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3)

    def test_cell_not_active(self):
        cell = Cell(multiplier=2, multiplier_type=True, active=False)
        letter = Tile(letter='P', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3)

if __name__ == '__main__':
    unittest.main()