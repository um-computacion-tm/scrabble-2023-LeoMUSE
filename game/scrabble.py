from game.board import Board
from game.player import Player
from game.bagtile import BagTiles
from game.tile import Tile

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
            self.players.append(Player())

    def start_game(self):
        for player in self.players:
            tilesToDraw = 7 - len(player.tiles)
            newTiles = self.bag_tiles.take(tilesToDraw)
            player.tiles.extend(newTiles)