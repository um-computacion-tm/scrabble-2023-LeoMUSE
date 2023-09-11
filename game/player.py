from game.tile import Tile

class Player:
    def __init__(self):
        self.tiles = []

    def play_word(self, word):
        if not all(tile in self.tiles for tile in word):
            raise ValueError("El jugador no tiene las fichas necesarias.")
        if all(tile in self.tiles for tile in word):
            for tile in word:
                self.tiles.remove(tile)
            return True

if __name__ == '__main__':
    pass