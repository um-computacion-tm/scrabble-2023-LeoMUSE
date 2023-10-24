from game.tile import Tile
from collections import Counter

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
        player_tiles = [tile.letter for tile in self.tiles]
        word_tiles = [tile.letter for tile in tiles]
        needed_tiles = Counter(word_tiles)

        for letter, count in needed_tiles.items():
            if player_tiles.count(letter) < count:
                return False
            
        return True
    
    def remove_letters(self, word):
        for letter in word:
            for tile in self.tiles:
                if tile == letter:
                    self.tiles.remove(tile)
                    break
    
    def assign_wildcard_value(self,letter, value):
        for tile in self.tiles:
            if tile.value == 0:
                self.tiles.remove(tile)
                new_tile = Tile(letter, value)
                self.tiles.append(new_tile)
            return True
    
    def get_score(self):
        return self.score
    
    def get_tiles(self):
        return self.tiles

if __name__ == '__main__':
    pass