from game.scrabble import ScrabbleGame
from game.player import Player
from game.bagtile import BagTiles

def is_valid_number_of_players(num):
    return 1 <= num <= 4

def validate_number_of_players():
    while True:
        try:
            players = int(input("Ingrese el numero de jugadores (2-4): "))
            if is_valid_number_of_players(players):
                return players
            else:
                print("El numero de jugadores debe estar entre 2 y 4.")
        except ValueError:
            print("Por favor, ingrese un numero valido.")

def main():
    print("¡Bienvenido a Scrabble!")

    players = validate_number_of_players()
    scrabble_game = ScrabbleGame(players)
    scrabble_game.start_game