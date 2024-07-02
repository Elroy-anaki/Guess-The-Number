import time
from Player import * 
from functions import *

def get_players():
    """
    Creates and returns a list of Player objects based on user input for the number of players.
    
    :return: A list of Player objects.
    """
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        player_name = input(f"Player {i + 1}: ")
        players.append(Player(player_name, points=0))
    return players

def main():
    print("Welcome to 'Guess The Number'!")
    
    try:
        # Define the word list by path of json file and category
        category = input("Enter category please: ").title()
        words_list = load_words(r'C:\Users\elroy\OneDrive\שולחן העבודה\Development\Python\Projects\Guess the number\words.json', category)
    except FileNotFoundError:
        print("The JSON file was not found. Please check the file path and try again.")
        return
    except json.JSONDecodeError:
        print("Error decoding the JSON file. Please check the file format and try again.")
        return

    count_of_numbers = check_valid_count_of_numbers(len(words_list), int(input("How many words do you want to guess? ")))

    # Define the players
    players = get_players()

    time.sleep(1)
    print(f"OK, let's start\nThe category is: {category}")
    number_of_word = 1
    for word in words_list[:count_of_numbers]:
        hidden_word = word.lower()

        for player in players:
            player.hidden_word = hidden_word
            player.old_guesses = []

        time.sleep(3)
        print(f"\nWord {number_of_word}:")
        print(secret_word(hidden_word))

        word_guessed = False
        while not word_guessed:
            for player in players:
                print()
                user_guess = input(f"{player.name}, your turn.\nYour guess: ")
                get_guess_from_user(user_guess, player.old_guesses, hidden_word)
                player.hidden_word = hidden_word_status(hidden_word, player.old_guesses)
                print(player.hidden_word)
                # Check if this player won
                if player.hidden_word.replace(' ', '') == hidden_word:
                    player.add_point()
                    time.sleep(2)
                    print(f"{player.name} won this word!")
                    word_guessed = True
                    break

        number_of_word += 1  

    # Checks who won the game   
    time.sleep(3)
    print("The score is:")
    for player in players:
        print(f"{player.name}: {player.points} points.")

    time.sleep(3)
    max_points = max(player.points for player in players)
    winners = [player.name for player in players if player.points == max_points]

    if len(winners) > 1:
        print(f"{', '.join(winners)} are the winners!!!")
    else:
        print(f"{winners[0]} is the winner!!!")

if __name__ == "__main__":
    main()
