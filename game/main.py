from game.scrabble import ScrabbleGame
from game.board import Board

def get_player_count():
    while True:
        try:
            player_count = int(input('Cantidad de jugadores (1-3): '))
            if 1 <= player_count <= 3:
                break
            else:
                print('Número de jugadores no válido. Intente de nuevo.')
        except ValueError:
            print('Ingrese un número válido por favor.')

    return player_count

def show_board(self):
    return Board.display_board()

def show_player(self):
    return ScrabbleGame.get_current_player()

def get_inputs():
    word = input('Palabra: ')
    coords_str = input('Coordenadas (fila, columna): ')
    coords_str = coords_str.replace('(', '').replace(')', '')
    coords_str = coords_str.strip()
    coords = tuple(map(int, coords_str.split(',')))
    orientation = input('Orientación (H/V): ')
    return word, coords, orientation

# def main():
#     player_count = get_player_count()
#     game = ScrabbleGame(player_count)
#     board = Board()
#     board.display_board
#     game.start_game()
#     while not game.is_game_over():
#         board.display_board(game.board)
#         game.display_rack(game.get_current_player())
#         word, coords, orientation = get_inputs()
#         try:
#             game.play(word, coords, orientation)
#         except Exception as e:
#             print(e)

if __name__ == '__main__':
    # main()
    pass