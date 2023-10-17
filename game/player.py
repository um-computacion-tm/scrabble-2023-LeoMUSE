from game.tile import Tile

class InsufficientTilesInHand(Exception):
    pass

class Player:
    def __init__(self):
        self.tiles = []
        self.passed_turn = False
        self.score = 0

    def __str__(self):
        tile_strings = [str(tile) for tile in self.tiles]
        return ", ".join(tile_strings)
    
    def pass_turn_player(self):
        self.passed_turn = True
        
    def validate_tiles_in_word(self, tiles=[]):
        player_tiles = [tile.letter.upper() for tile in self.tiles]
        word_tiles = [tile.letter.upper() for tile in tiles]
        needed_tiles = {}
        
        for letter in word_tiles:
            if letter in needed_tiles:
                needed_tiles[letter] += 1
            else:
                needed_tiles[letter] = 1
        
        for letter, count in needed_tiles.items():
            if player_tiles.count(letter) < count:
                raise InsufficientTilesInHand(f"No tienes los tiles necesarios")
        
        return True
    
    def assign_wildcard_value(self,letter, value):
        for tile in self.tiles:
            if tile.value == 0:
                self.tiles.remove(tile)
                new_tile = Tile(letter, value)
                self.tiles.append(new_tile)
            return True
    
if __name__ == '__main__':
    pass