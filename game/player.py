from game.tile import Tile

class Player:
    def __init__(self):
        self.tiles = []
        self.passed_turn = False

    def __str__(self):
        tile_strings = [str(tile) for tile in self.tiles]
        return ", ".join(tile_strings)
    
    def pass_turn_player(self):
        self.passed_turn = True
    
    def play_word(self, word):
        if not all(tile in self.tiles for tile in word):
            raise ValueError("El jugador no tiene las fichas necesarias.")
        if all(tile in self.tiles for tile in word):
            for tile in word:
                self.tiles.remove(tile)
            return True

    def assign_wildcard_value(self,letter, value):
        for tile in self.tiles:
            if tile.value == 0:
                self.tiles.remove(tile)
                new_tile = Tile(letter, value)
                self.tiles.append(new_tile)
            return True
        
    def mostrar_atril(self):
        print("Atril del Jugador:")
        for index, tile in enumerate(self.tiles, start = 1):
            print(f"{index}: {tile}")
    
if __name__ == '__main__':
    pass