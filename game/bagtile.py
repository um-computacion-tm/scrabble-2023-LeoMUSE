import random
from game.tile import Tile

class BagTiles:
    def __init__(self):
        tile_counts = {
            (' ', 0): 2,
            ('A', 1): 12,
            ('E', 1): 12,
            ('I', 1): 6,
            ('L', 1): 6,
            ('N', 1): 5,
            ('O', 1): 8,
            ('R', 1): 7,
            ('S', 1): 6,
            ('T', 1): 5,
            ('U', 1): 5,
            ('D', 2): 5,
            ('G', 2): 2,
            ('B', 3): 2,
            ('C', 3): 5,
            ('M', 3): 2,
            ('P', 3): 2,
            ('F', 4): 1,
            ('H', 4): 3,
            ('V', 4): 1,
            ('Y', 4): 1,
            ('Q', 5): 1,
            ('J', 8): 1,
            ('Ñ', 8): 1,
            ('X', 8): 1,
            ('Z', 10): 1,
        }
    
        self.initial_tile_count = 103

        self.tiles = [Tile(letter, value) for (letter, value), count in tile_counts.items() for _ in range(count)]
        random.shuffle(self.tiles)

    def __str__(self):
        return f"Tiles in bag: {len(self.tiles)}"

    def tiles_in_bag(self):
        return len(self.tiles)
        
    def take(self, count):
        if count > len(self.tiles):
            raise ValueError("No hay suficientes fichas en la bolsa.")
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
        self.initial_tile_count += len(tiles)
        random.shuffle(self.tiles)

if __name__ == '__main__':
    pass