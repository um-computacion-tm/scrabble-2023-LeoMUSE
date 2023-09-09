from game.scrabble import ScrabbleGame
from game.player import Player
from game.bagtile import BagTiles

def is_valid_number_of_players(num):
    return 1 <= num <= 4

def get_inputs():
    while True:
        try:
            players = int(input("Ingrese el numero de jugadores (2-4): "))
            if 1 <= players <= 4:
                return players
        except ValueError:
            print("Por favor, ingrese un numero valido.")

def validate_number_of_players():
    while True:
        players = get_inputs()
        if is_valid_number_of_players(players):
            return players
        else:
            print("Por favor, ingrese un numero valido (2-4).")

def main():
    print("¡Bienvenido a Scrabble!")

    players = validate_number_of_players()
    scrabble_game = ScrabbleGame(players)
    scrabble_game.start_game

if __name__ == '__main__':
    main()