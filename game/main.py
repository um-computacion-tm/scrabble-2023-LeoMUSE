from game.scrabbleCli import ScrabbleCli

def main():
    cliente = ScrabbleCli(player_count = 0)
    cliente.start_game()

if __name__ == '__main__':
    main()