# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

## [0.0.1] - 2023-08-19

- Code we did in class

## [0.0.2] - 2023-08-20

- Completed the tile bag

## [0.0.3] - 2023-08-23

- Modify Tilebag changed to 1 single Tile with the amount

## [0.0.4] - 2023-08-26

- Added game/board base code
- Added game/cell base code
- Added game/player base code
- Added game/scrabble base code
- Added Test for each ./game/ archive

## [0.0.5] - 2023-08-28

- Added start game metod in game/scrabble

## [0.0.6] - 2023-08-29

- Added play word metod in game/player

## [0.0.7] - 2023-08-31

- separate models.py into bagtiles.py and tiles.py
- Added metod to calculate word value base

## [0.0.8] - 2023-09-03

- Added metod to change turn

## [0.0.9] - 2023-09-07

- Added metod to verify orientation in board.py

## [0.1.0] - 2023-09-09

- Added Base main and tests for mian

## [0.1.1] - 2023-09-11

- Added Raises ValueError for some metods.

## [0.1.2] - 2023-09-12

- Added all metod ralated to time in turns

## [0.1.3] - 2023-09-18

- Added property is_empty to board.py
- Deleted all main to try one better.
- Deleted all main tests sice they are irrelevant.

## [0.1.4] - 2023-09-19

- Added Metod to define Wildcard letter and value.

## [0.1.5] - 2023-09-22

- Added Dictionary class.
- Added metod to check word if it is in dicionary.txt.
- Added dictionary.txt

## [0.1.6] - 2023-09-23

- Added pass_turn metod to players and scrabble.

## [0.1.7] - 2023-09-24

- Added put_word_horizontal metod.

## [0.1.8] - 2023-09-26

- Added metod to get a game over.

## [0.1.9] - 2023-10-1

- Added display rack.

## [0.2.0] - 2023-10-2

- Moved display_rack to scrabble.py
- Added display_board in scrabble.py

## [0.2.1] - 2023-10-5

- Added Part of main (made in class).
- Added Play metod to scrabble.py (made in class).
- Added validate word to scrabble.py (commented) (made in class).

## [0.2.2] - 2023-10-6

- Added multipliers cordenates in board.
- Modify calculate word value to use "word"
- Modify calculate value (letter) to use "letter"

## [0.2.3] - 2023-10-8

- Moved display_board to board.py.
- Modify display_board.
- Added to diplay_board show the multipliers.

## [0.2.4] - 2023-10-8

- Added to display_board the form to replace a multiplier for a letter if the cell has a letter.
- repared the metodo to validate_tiles_in_word to verify if the player has the tiles.

## [0.2.5] - 2023-10-16

- Modified some varied lines of code.

## [0.2.6] - 2023-10-17

- Added metod to play word the first time.

## [0.2.7] - 2023-10-19

- Modified put_word metod
- Added validate word conected metod.

## [0.2.8] - 2023-10-21 

- Added metodod to to verify that the word dont overlap letterts that already are in the board.

## [0.2.9] - 2023-10-22

- Repared function show_board of main.py .

## [0.3.0] - 2023-10-24

- Added metod to remove the tiles from the player that used the word.
- Added __eq__ to tile to comparate from letter and value and not the memory directory.

## [0.3.1] - 2023-10-25

- Modified Validate_tiles_in_word metod
- Modified put_word_first_time
- Repared tests

## [0.3.2] - 2023-10-27

- Added metod get_word_cells
- Modified put_word metod
- Added metod word_to_cells
- Repared tests

## [0.3.3] - 2023-10-28

- Create scrabbleCli.py
- Added metod get_player_count
- Added metod to draw_tiles
- Separated start_game in scrabble in give_tiles give_initial_tiles_to_players
- Modified is_game_over
- Repared Tests

## [0.3.4] - 2023-10-29

- Moved metod Show_board
- Added metod Show_tiles
- Added metod Show_score

## [0.3.5] - 2023-11-30

- Added metod get_tiles_in_board
- Added metod Play_word
- Added metod get_tiles 

## [0.3.6] - 2023-11-1

- Added metod start_game
- Added metod player_turn
- Added metod skip_turn
- Added metod quit

## [0.3.7] - 2023-11-2

- Added metod get_word_location_orientation
- Added metod place_and_put_word
- Added metod play_first_word
- Added metod play_word_not_first_time

## [0.3.8] - 2023-11-4

- Added metod exchange
- Added metod force_skip
- Added metod play_jocker

## [0.3.9] - 2023-11-5

- Repared tests
- Repared validate_tiles_in_word
- Repared play_word
- Repared put_word
- Added staticmetod to convert word(str) to tiles(object)

## [0.4.0] - 2023-11-6

- Repared player using tiles in board to complete the word
- Repared calculate_word_score
- Added calculate_score in scrabble.py
- Repared show_score

## [0.4.1] - 2023-11-7

- Added Dockerfile
- Modified README.md
- Repared tests
- Repared metod exchange_tiles
