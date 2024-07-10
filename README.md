# Game - Guess the Word

## Overview
"Guess the Word" is a simple multiplayer game where players take turns guessing letters to uncover a hidden word. The game progresses through rounds until all words in the word bank have been guessed, and the player with the most points wins.

## Core Functionality

1. The game selects a word unknown to both players and displays it with all letters replaced by underscores (_).
2. Player 1 guesses a letter:
   - If the letter is in the word, the game replaces the underscores with the letter in the correct positions and the player earns a point.
   - If the letter is not in the word, the game notifies the player.
3. The game displays the word with guessed letters revealed and switches to the next player.
4. The process repeats until the word is fully guessed.
5. A new word is selected, and the game continues until all words are guessed.

## Full Requirements

- The game runs from the command line using `argparse` or a similar library.
- Parameters:
  - Path to the file with the word list.
  - Number of players.
- Round details:
  - The partially guessed word is displayed.
  - Each correctly guessed letter appears; all other letters remain hidden.
  - The current player guesses a letter:
    - Input must be a single letter.
    - If the letter was previously guessed, the player must guess again.
    - If the letter is in the word, the player earns a point.
- The game is case-insensitive.
- When a word is fully guessed, a new word is selected, and guessed letters are reset.
- The game ends when all words are guessed, and the player with the most points wins.

## Extra Features

- Use player names instead of "Player 1", "Player 2", etc.
- Display the category or hint for each word.
- Award points for each occurrence of a correctly guessed letter in the word.
- Load the word list from a JSON file.
- Set the number of words in the game via the command line:
  - The game ends after the specified number of words are guessed.
  - If the file contains fewer words than specified, notify the players and end the game.

## Usage

To start the game, use the following command:

```bash
python guess_the_word.py --wordlist path/to/wordlist.json --players int
