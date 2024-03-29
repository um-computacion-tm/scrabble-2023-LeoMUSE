from game.scrabble import ScrabbleGame, NoValidWordException, NoLettersExeption
from game.player import Player
from game.board import NoCenterLetterException , NoWordConnectedException


class ScrabbleCli:
    def __init__(self, player_count):
        self.game = ScrabbleGame(players_count=player_count)
        self.first_time = True
        self.quit_game = False

    def get_player_count(self):
        while True:
            try:
                player_count = int(input('Ingrese un numero de jugadores (2-4): '))
                if 2 <= player_count <= 4:
                    self.game.players = [Player() for _ in range(player_count)]
                    return player_count
                else:
                    print('Ingrese un numero entre 2 y 4.')
            except ValueError:
                print('Ingrese un numero.')

    def start_game(self):
        print("¡¡Bienvenido a Scrabble!!")
        self.game.game_state = 'jugando'
        player_count = self.get_player_count()

        if player_count == 0:
            return
        
        while not self.game.is_game_over():

            print("----------------------------------------------------------------------------------------------------------------")
            print(f'ROUND N°{self.game.round}')
            print("----------------------------------------------------------------------------------------------------------------")            

            self.draw_tiles()
            self.show_board()

            print("----------------------------------------------------------------------------------------------------------------")
            self.show_tiles(player=self.game.current_player)
            print("----------------------------------------------------------------------------------------------------------------")
            self.player_turn()

            self.game.round += 1

            if self.quit_game:
                break

    def draw_tiles(self):
        current_player = self.game.players[self.game.current_player]
        if len(current_player.tiles) == 0:
            self.game.give_initial_tiles_to_all_players()
        else:
            if len(current_player.tiles) < 7:
                needed_tiles = 7 - len(current_player.tiles)
                self.game.give_tiles(self.game.current_player, needed_tiles)

    def show_tiles(self,player):
        tiles = self.game.players[self.game.current_player].show_tiles()
        tiles_str = ", ".join([str(tile) for tile in tiles])
        print(f"Fichas: [{tiles_str}] del jugador {self.game.current_player}")

    def show_board(self):
        board_state = self.game.board.display_board()
        print(board_state)

    def show_scores(self):
        print("Puntuacion del Player")
        print("--------------------")
        for index, player in enumerate(self.game.players):
            player_score = player.get_score()
            print(f"{index:<12} {player_score:<10}")

    def player_turn(self):
        self.draw_tiles()
        is_turn_finished = False
        while not is_turn_finished:
            action = input(' 1) Jugar Turno / 2) Mostrar Puntajes / 5) Salir ')
            action = self.game.comprobate_is_a_number(action)
            if action == 1:
                is_turn_finished = self.playing()
            elif action == 2:
                self.show_scores()
            elif action == 5:
                self.quit()
                break

    def playing(self, action_input=None):
        self.draw_tiles()
        actions = {1: self.place_and_put_word, 2: self.exchange, 3: self.play_joker, 4: self.skip_turn}
        while not self.quit_game:
            if action_input is None:
                action = input(' 1) Jugar Palabra / 2) Cambiar Fichas / 3) Usar Jocker / 4) Pasar Turno ')
            else:
                action = action_input
            action = self.game.comprobate_is_a_number(action)
            action_function = actions.get(action)
            if action_function is None:
                print('Debe Seleccionar una accion.')
            else:
                try:
                    if action_function():
                        return True
                except NoWordConnectedException:
                    print('La palabra tiene que estar conectada. Inténtalo de nuevo.')
                
    def play_joker(self):
        current_player = self.game.players[self.game.current_player]
        tiles = current_player.tiles

        if not any(tile.letter == ' ' for tile in tiles):
            print("No tienes un Joker (' ').")
            return

        while True:
            letter_choice = input("Qué letra quieres para el joker (' '): ").strip().upper()

            if len(letter_choice) != 1 or not letter_choice.isalpha():
                print("Letra inválida, elija una de (A-Z).")
                continue

            joker_tile = next((tile for tile in tiles if tile.letter == ' '), None)

            if joker_tile:
                joker_tile.letter = letter_choice
                joker_tile.value = 0
                print('----------------------------------------------------------------------------------------------------------------')
                self.show_tiles(current_player)
                print('----------------------------------------------------------------------------------------------------------------')                
                break
                
    def place_and_put_word(self):
        while True:
            try:
                word, location, orientation = self.get_word_location_orientation()
                if word == '0':
                    break
                if self.first_time == True:
                    self.place_first_word(word, location, orientation)
                else:
                    self.place_word_not_first_time(word, location, orientation)
                return 'terminar'
            except (NoValidWordException, NoLettersExeption) as e:
                print(f'Error: {e}')
                validate = input('Puedes Volver usando el 0: ')
                if validate == '0':
                    break

    def place_first_word(self, word, location, orientation):
        try:
            success = self.game.play_word(word,location,orientation, self.game.players[self.game.current_player].tiles)
            if success:
                self.game.put_on_the_board_first_time(word, location, orientation)
                print("Palabra colocada exitosamente en el centro.")
                self.draw_tiles()
                self.first_time = False
        except NoCenterLetterException as f:
            print(f'Error: {f}')
            validate = input('Puedes Volver usando el 0: ')
            if validate == '0':
                return 

    def place_word_not_first_time(self, word, location, orientation):
        if self.game.play_word(word,location,orientation, self.game.players[self.game.current_player].tiles): 
            player = self.game.players[self.game.current_player]
            new_tiles = self.game.bag_tiles.take(len(word))
            player.get_tiles(self.game.bag_tiles, len(new_tiles))
            self.game.put_word_not_first_time(word, location, orientation)
            self.draw_tiles()
            print("Palabra colocada exitosamente.")

    def get_word_location_orientation(self):
        while True:
            word = input('Ingrese una Palabra (0 para Pasar): ')
            if word == '0':
                return word, None, None
            
            location_x = None
            location_y = None

            while location_x is None or location_y is None:
                location_x_input = input('Fila (0-14): ')
                location_x = self.game.comprobate_is_a_number(location_x_input)
                if location_x is None:
                    print('¡¡Fila tiene que ser un número!!')
                elif not (0 <= location_x <= 14):
                    print('La fila debe estar entre 0 y 14.')
                    location_x = None

                location_y_input = input('Columna (0-14): ')
                location_y = self.game.comprobate_is_a_number(location_y_input)
                if location_y is None:
                    print('¡¡Columna tiene que ser un número!!')
                elif not (0 <= location_y <= 14):
                    print('La columna debe estar entre 0 y 14.')
                    location_y = None

            location = (location_x, location_y)
            
            orientation = input('Orientación (V/H): ')
            orientation = orientation.strip().upper()
            orientation = self.game.comprobate_is_an_orientation(orientation)
            return word, location, orientation
            
    def exchange(self):
        player = self.game.players[self.game.current_player]
        
        while True:
            tiles_to_exchange = input("Elija qué fichas quiere cambiar (ingrese números del 1 al 7 separados por espacios, o '0' para no cambiar ninguna): ")
            
            if tiles_to_exchange == '0':
                break 

            selected_indices = self.get_selected_indices(tiles_to_exchange, player)
            
            if selected_indices:
                exchanged_tiles, new_tiles = player.exchange_tiles(self.game.bag_tiles, selected_indices)
                self.print_exchange_results(exchanged_tiles, new_tiles, player)
                self.force_skip()
                break

    def get_selected_indices(self, tiles_to_exchange, player):
        selected_indices = []
        tiles = tiles_to_exchange.split()
        
        for tile in tiles:
            if tile.isnumeric():
                index = int(tile) - 1
                if 0 <= index < len(player.tiles):
                    selected_indices.append(index)
                else:
                    print("Índice fuera de rango. Intente nuevamente.")
            else:
                print("Entrada inválida. Ingrese números separados por espacios o '0' para no cambiar fichas.")
        
        return selected_indices

    def print_exchange_results(self, exchanged_tiles, new_tiles, player):
        print('----------------------------------------------------------------------------------------------------------------')
        print(f"Fichas Cambiadas: {[tile for tile in exchanged_tiles]}")
        print('----------------------------------------------------------------------------------------------------------------')
        print(f"Nuevas Fichas: {[tile for tile in new_tiles]}")
        print('----------------------------------------------------------------------------------------------------------------')
        print(f'Nuevas Fichas: {player.tiles}')

    def force_skip(self):
        self.game.next_turn()
        self.game.round += 1

        print("----------------------------------------------------------------------------------------------------------------")
        print(f'ROUND N°{self.game.round}')
        print("----------------------------------------------------------------------------------------------------------------")            
  
        self.show_board()
        print("----------------------------------------------------------------------------------------------------------------")    
        self.show_tiles(player=Player) 
        print("----------------------------------------------------------------------------------------------------------------")

    def skip_turn(self):
        self.game.round += 1
        response = input("¿Quieres saltar el turno? (S/N): ")
        if response.upper() == "S":
            print("----------------------------------------------------------------------------------------------------------------")
            print(f'ROUND N°{self.game.round}')
            print("----------------------------------------------------------------------------------------------------------------")            
            
            self.game.next_turn()
            
            active_player = self.game.players[self.game.current_player]
            
            self.show_board()
            print("----------------------------------------------------------------------------------------------------------------")    
            self.show_tiles(player=active_player)
            print("----------------------------------------------------------------------------------------------------------------")    
        else:
            return "Ingrese una Palabra."

    def quit(self):
        response = input("¿Estás seguro de que quieres salir del juego? (S/N): ")
        if response.strip().upper() == "S":
            self.quit_game = True

if __name__ == '__main__':
    pass