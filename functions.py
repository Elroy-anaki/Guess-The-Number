import json 


def load_words(file_path, string):
    """
    Loads the words from json file and checks the category 
    
    :params file_path: file path to the json file
    :params string: category from the file
    :return: A list of words
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        while string not in data:
            print("This category doesn't exist! Try again.")
            string = input("Enter category please: ").strip().title()
        list = data[string]
        return list
    
    
def check_valid_count_of_numbers(num1, num2):
    """
    Forces the user to enter a correct number of words they want to guess 
    
    :params num1: Count of words in the file
    :params num2: Number that comes from the user
    return: A number
    """
    while num2 > num1:
        print("There are no so many numbers in the words list, Try again.")
        num2 = int(input("How many words do you want to guess? "))
    return num2


def secret_word(word):
    """
    Creates a string of underscores ('_ ') representing the hidden word.
    
    :param word: A string representing the hidden word.
    :return: A string of underscores of the same length as the hidden word.
    """
    return '_ ' * len(word)


def check_invalid_input(letter_guessed, old_guesses):
    """
    Checks if the user's input is valid: only letters, single character, and not guessed before.
    
    :param letter_guessed: The guessed letter.
    :param old_guesses: A list of previously guessed letters.
    :return: A tuple (bool, str) where the boolean indicates validity and the string contains the error message if invalid.
    """
    if not letter_guessed.isalpha():
        return False, "Invalid input! (only letters a - z)"
    if len(letter_guessed) > 1:
        return False, "Invalid input! (only single letter)"
    if letter_guessed.lower() in old_guesses:
        return False, "You already guessed this letter"
    
    return True, ""


def fix_guess(letter_guessed, old_guesses):
    """
    Ensures the guessed letter is valid by repeatedly prompting the user until a valid guess is provided.
    
    :param letter_guessed: The initially guessed letter.
    :param old_guesses: A list of previously guessed letters.
    :return: A valid guessed letter.
    """
    valid, message = check_invalid_input(letter_guessed, old_guesses)
    while not valid:
        print(message)
        letter_guessed = input("Try again\nYour guess: ")
        valid, message = check_invalid_input(letter_guessed, old_guesses)
    return letter_guessed


def get_guess_from_user(letter_guessed, old_guesses, hidden_word):
    """
    Gets a valid guess from the user and updates the list of old guesses.
    
    :param letter_guessed: The initially guessed letter.
    :param old_guesses: A list of previously guessed letters.
    :param hidden_word: The hidden word being guessed.
    """
    guess = fix_guess(letter_guessed, old_guesses)
    if guess not in hidden_word:
        print("Incorrect guess.")
    old_guesses.append(guess.lower())


def hidden_word_status(hidden_word, old_guesses):
    """
    Returns the current status of the hidden word with guessed letters revealed.
    
    :param hidden_word: The hidden word being guessed.
    :param old_guesses: A list of previously guessed letters.
    :return: A string representing the current status of the hidden word.
    """
    current_guess = ['']
    for letter in hidden_word:
        if letter in old_guesses:
            current_guess.append(letter + " ")
        else:
            current_guess.append("_ ")
    result = ''.join(current_guess)
    return result
