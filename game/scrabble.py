from game.board import Board
from game.player import Player
from game.bagtile import BagTiles
from game.tile import Tile
import time
import threading

class ScrabbleGame:
    def __init__(self, players_count,):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.player = Player()
        self.players = []
        self.current_player = 0
        self.turn_limit = 60
        for _ in range(players_count):
            self.players.append(Player())

    def get_current_player(self):
            return self.players[self.current_player]

    def start_game(self):
        for player in self.players:
            tilesToDraw = 7 - len(player.tiles)
            newTiles = self.bag_tiles.take(tilesToDraw)
            player.tiles.extend(newTiles)

    def next_turn(self):
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def pass_turn_scrabble(self, player_index):
        current_player = self.players[self.current_player]
        current_player.pass_turn_player()
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0

    def is_game_over(self):
        if len(self.bag_tiles.tiles) == 0 and not self.can_exchange_tiles():
            return True
        
    def can_exchange_tiles(self):
        current_player = self.players[self.current_player]
        exchangeable_tiles = [tile for tile in current_player.tiles if tile.letter != '' and tile.value != 0]
        return len(exchangeable_tiles) > 0

    def set_time_limit(self, time_limit):
        self.turn_limit = time_limit
    
    def start_timer(self):
        threading.Thread(target = self._timer_thread).start()

    def _timer_thread(self):
        current_player = self.players[self.current_player]
        start_time = time.time()
        while time.time() - start_time < self.turn_limit:
            time.sleep(1)
        print(f"Tiempo agotado para {current_player} - Turno perdido.")
        self.next_turn()
        
    def display_rack(self, player):
        for i in player.tiles:
            print(f'[{i.letter},{i.value}]', end=' ')

    def display_board(self, board):
        print("Tablero de Scrabble:")
        for row in board.grid:
            for cell in row:
                if cell.letter is not None:
                    print(f"[{cell.letter.letter}]", end=' ')
                else:
                    print("[ ]", end=' ')
            print()

    # def validate_word(self, word, location, orientation):
    #     if not self.player.validate_tiles_player(word):
    #         raise ValueError("El jugador no tiene las fichas necesarias.")
    #     if not self.board.check_word(word):
    #         raise ValueError("Su palabra no existe en el diccionario")
    #     if not self.board.validate_word_inside_board(word, location, orientation):
    #         raise ValueError("Su palabra excede el tablero")
        
    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_word(word, location, orientation)
        total = self.board.calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

if __name__ == '__main__':
    pass