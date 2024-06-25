import time
from Player import * 
from functions import *


def main():
    print("Welcome to 'Guess The Number'!")
    # Define the word list by path of json file
    print(r"The file path is: 'C:\Users\elroy\OneDrive\שולחן העבודה\Development\Python\Projects\Guess the number\words.json' ")
    file_path = input("Enter the file path please: ")
    category = input("Enter category please: ").title()
    words_list = load_words(file_path, category )
    count_of_numbers = check_valid_count_of_numbers(len(words_list), int(input("How many words do you want to guess? ")))
    # Define the players and their name
    player1 = Player(input("Player 1: "), points=0)
    player2 = Player(input("Player 2: "), points=0)

    time.sleep(1) 
    print(f"OK, let's start\nThe category is: {category}")
    number_of_word = 1
    for word in words_list[:count_of_numbers]:
        
        # Define the word as the hidden word
        hidden_word = word.lower()
        
        # Define the hidden word and the old guesses for each player
        player1.hidden_word = hidden_word
        player1.old_guesses = []
        player2.hidden_word = hidden_word
        player2.old_guesses = []
        time.sleep(3) 
        print(f"\nWord {number_of_word}:")
        print(secret_word(hidden_word))
        
        while True:
            # The game:
            # Player 1
            print()
            user_guess = input(f"{player1.name}, your turn.\nYour guess: ")
            get_guess_from_user( user_guess,player1.old_guesses, hidden_word)
            player1.hidden_word = hidden_word_status(hidden_word, player1.old_guesses)
            print(player1.hidden_word)
            # Check in every iteration if this player won
            if player1.hidden_word.replace(' ', '') == hidden_word:
                player1.add_point()
                time.sleep(2)
                print(f"{player1.name} won in this word!")
                break
            
            # Player 2
            print()
            user_guess = input(f"{player2.name}, your turn\nYour guess: ")
            get_guess_from_user( user_guess,player2.old_guesses, hidden_word)
            player2.hidden_word = hidden_word_status(hidden_word, player2.old_guesses)
            print(player2.hidden_word)
            # Check in every iteration if this player won    
            if player2.hidden_word.replace(' ', '') == hidden_word:
                player2.add_point()
                time.sleep(2)
                print(f"{player2.name} Won in this word!")
                break
                
        number_of_word += 1  
              
    # Checks who won the game   
    time.sleep(3) 
    print("The score is:")
    print(f"{player1.name}: {player1.points} points.")      
    print(f"{player2.name}: {player2.points} points.")   
    print("So....") 
    time.sleep(3)  
    if player1.points > player2.points:
        print(f"{player1.name} is the winner!!!")
    elif player1.points == player2.points:
        print(f"Two players are winners!!!")
    else:
        print(f"{player2.name} is the winner!!!")
            
if __name__ == "__main__":
    main()