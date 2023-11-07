from game.tile import Tile
from collections import Counter
from game.bagtile import BagTiles

class InsufficientTilesInHand(Exception):
    pass

class Player:
    def __init__(self):
        self.tiles = []
        self.passed_turn = False
        self.score = 0
    
    def pass_turn_player(self):
        self.passed_turn = True
        
    def validate_tiles_in_word(self, word, tiles=[]):
        player_letter_tiles = []
        for tile in tiles:
            player_letter_tiles.append(tile.letter)
        player_letter_quantities = {}
        for l in player_letter_tiles:
            if l in player_letter_quantities:
                player_letter_quantities[l] += 1
            else:
                player_letter_quantities[l] = 1
        word_letter_count = {}
        for l in word:
            if l.upper() in word_letter_count:
                word_letter_count[l.upper()] += 1
            else:
                word_letter_count[l.upper()] = 1
        for letter, count in word_letter_count.items():
            if letter.upper() not in player_letter_quantities or player_letter_quantities[letter.upper()] < count:
                return False
        return True
    
    def has_letter(self, word): 
        tiles = [tile.letter for tile in self.tiles]
        for letter in word:
            if letter in tiles:
                tiles.remove(letter)
            else:
                return False
        return True
    
    def remove_letters(self, word):
        if self.has_letter(word):
            played_tiles = []
            for letter in word:
                for tile in self.tiles:
                    if tile.letter == letter:
                        played_tiles.append(tile)
                        self.tiles.remove(tile)
                        break
            return played_tiles
        else:
            return False
    
    def exchange_tiles(self, bag, tiles_to_exchange):
            exchanged_tiles = [self.tiles[index] for index in tiles_to_exchange]
            for index in sorted(tiles_to_exchange, reverse=True):
                del self.tiles[index]
            new_tiles = bag.take(len(exchanged_tiles))
            self.tiles.extend(new_tiles)
            return exchanged_tiles, new_tiles
    
    def add_score(self, amount):
        self.score += amount

    def get_score(self):
        return self.score
    
    def show_tiles(self):
        return self.tiles
    
    def get_tiles(self, bag: BagTiles, amount):
        amount = 7 - len(self.tiles)
        self.tiles.extend(bag.take(amount))

if __name__ == '__main__':
    pass