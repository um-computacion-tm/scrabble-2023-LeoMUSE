from game.board import Board
from game.player import Player
from game.bagtile import BagTiles
from game.tile import Tile

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.current_player = 0
        for _ in range(players_count):
            self.players.append(Player())

    def start_game(self):
        for player in self.players:
            tilesToDraw = 7 - len(player.tiles)
            newTiles = self.bag_tiles.take(tilesToDraw)
            player.tiles.extend(newTiles)

    def next_turn(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

if __name__ == '__main__':
    pass