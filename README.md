 # Scrabble:

SCRABBLE® is a crossword game for 2, 3 or 4 players. It consists of forming words on the board that intersect with each other, just like in crossword puzzles, using pieces marked with a letter AND a number.

## How To use:

- HOW TO USE:
```
sudo pat-get install git
```
- Clone the repositorie.
```
git clone https://github.com/um-computacion-tm/scrabble-2023-LeoMUSE.git
```
- Install Docker.
```
docker build -t [image name] .
```
- Go to the file address.
```
cd (where you put it)/scrabble-2023-LeoMUSE
```
- Run it.
```
docker run -it [image name]
```
- This project use pyrae to validate the word in the dictionary so use internet to validate.

## How to run test:
```
coverage run -m unittest $$ coverage reṕrt -m
```
## RULES

The imputs mus be always in mayus
When you put a word using letter of the board YOU MUST give the complete word and location orientation that coincide whit the tile in board

### TILES

- O point: Joker in hand, in board the letter value
- 1 Point: A, E, I, O, U, L, N, R, S, T
- 2 Points: D, G
- 3 Points: B, C, M, P
- 4 Points: F, H, V, Y
- 5 Points: Q
- 8 Points: J, Ñ, X
- 10 Points: Z

The board has multipliers

### TYPES OF MULTIPLIERS

- DL = Double Letter
- TL = Triple Letter
- DW = Double Word
- TW = Triple Word

## Game Develop Diary

- Go to: [CHANGELOG.md](https://github.com/um-computacion-tm/scrabble-2023-LeoMUSE/blob/main/CHANGELOG.md)

# ¡¡¡BADGES!!!!

## Main
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-LeoMUSE/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-LeoMUSE/tree/main)

## Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/031a39d495798a20ca98/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-LeoMUSE/maintainability)

## Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/031a39d495798a20ca98/test_coverage)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-LeoMUSE/test_coverage)

# Alumno

- Nombre: Leandro Flores
- Legajo: 59177
- User: LeoMUSE