from game.board import Board
from game.player import Player
from game.bagtile import BagTiles
from game.dictionary import word_in_dictionary

class NoLettersExeption(Exception):
    pass

class NoValidWordException(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.current_player = 0
        self.game_state = None
        self.round = 0

        for _ in range(players_count):
            self.players.append(Player())

    def get_current_player(self):
            return self.players[self.current_player]
    
    def give_initial_player_tiles(self, player_index):
        player = self.players[player_index]
        player.get_tiles(self.bag_tiles, 7)
        self.next_turn()

    def give_tiles(self, player_index, amount):
        player = self.players[player_index]
        if len(player.tiles) + amount > 7:
            amount = 7 - len(player.tiles)
        player.get_tiles(self.bag_tiles, amount)
        self.next_turn()

    def give_initial_tiles_to_all_players(self):
        for player_index in range(len(self.players)):
            self.give_tiles(player_index, amount = 7)

    def comprobate_is_an_orientation(self, orientation):
        real_orientation = ['H', 'V']
        if orientation in real_orientation:
            return orientation
        else:
            return None

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
        self.game_state = 'terminado'
        if (self.bag_tiles) == []:
            return True
        return False
    
    def game_state_start(self):
        self.game_state = 'jugando'
        
    def correct_word(self, word, location, orientation):
        if not word_in_dictionary(word):
            raise NoValidWordException('Palabra no existe')
        self.board.validate_crossing_words(word, location, orientation)
        self.board.validate_word_connected(word,location,orientation)
        return True
        
    def put_word_not_first_time(self, word, location, orientation):
        current_player = self.players[self.current_player]
        if self.correct_word(word, location, orientation):
            word_list = self.board.convert_word_to_tiles(word)
            self.board.put_word(word_list, location, orientation)
            self.calculate_score(word, location, orientation)
            current_player.remove_letters(word)
        self.next_turn()
        return True
    
    def put_on_the_board_first_time(self, word, location, orientation):
        current_player = self.players[self.current_player]
        if not word_in_dictionary(word):
            raise NoValidWordException('Palabra no existe')
        word_list = self.board.convert_word_to_tiles(word)
        self.board.put_word_first_time(word_list, location, orientation)
        self.calculate_score(word, location, orientation)
        current_player.remove_letters(word)
        self.next_turn()
        return True
    
    def comprobate_is_a_number(self, string):
        try:
            return int(string)
        except ValueError:
            return None
        
    def can_exchange_tiles(self):
        current_player = self.players[self.current_player]
        exchangeable_tiles = [tile for tile in current_player.tiles if tile.letter != '' and tile.value != 0]
        return len(exchangeable_tiles) > 0
    
    def calculate_score(self, word, location, orientation):
        player = self.get_current_player()
        word_cells = self.board.word_to_cells(word, location[0], location[1], orientation)
        word_value = self.board.calculate_word_value(word_cells, location, orientation)
        player.add_score(word_value)
    
    def get_tiles_on_board(self, word, location, orientation):
        board = self.board.grid
        tiles_on_board = []

        row, col = location

        for letter in word:
            if letter == ' ':
                continue 
            
            if orientation == 'H':
                cell = board[row][col]
            else:
                cell = board[row][col]

            if cell.tile is not None:
                tiles_on_board.append(cell.tile)

            if orientation == 'H':
                col += 1
            else:
                row += 1
        return tiles_on_board
            
    def play_word(self, word, location, orientation, tiles):
        player = self.players[self.current_player]

        tiles_on_board = self.get_tiles_on_board(word, location, orientation)

        player.tiles.extend(tiles_on_board)

        if player.validate_tiles_in_word(word, player.tiles):
            return True
        else:
            raise NoLettersExeption('No tienes las fichas necesarias')
        
if __name__ == '__main__':
    pass