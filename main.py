from hangman_words_real import words as word_list
from hangman_art import logo, stages
from string import ascii_lowercase
import random
import os
import time

def clear_screen():
    """
    Clear the terminal screen and print the hangman logo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def get_masked_word(word_to_mask : str, user_guesses : str):
    """
    Return a string where each character of word_to_mask is replaced with
    the corresponding character if it exists in user_guesses, otherwise replaced
    with "_".

    Parameters
    ----------
    word_to_mask : str
        The word to be masked.
    user_guesses : str
        The letters guessed by the user so far.

    Returns
    -------
    str
        The masked word.
    """
    return "".join([char if char in user_guesses else "_" for char in word_to_mask])

def play(secret_word : str):
    """
    Play a game of Hangman with a given secret word.

    Parameters
    ----------
    secret_word : str
        The word to be guessed.

    Returns
    -------
    bool
        True if the user guessed the word correctly, False otherwise.
    """
    user_guesses = []
    user_wrong_answers = []
    masked_word = get_masked_word(secret_word, user_guesses)
    total_lives = 6
    while total_lives:
        clear_screen()
        print(stages[total_lives])
        print(f'''Guess a letter of the word:
        {get_masked_word(secret_word, user_guesses)}''')
        user_answer = input(f"You have {total_lives} attempts left: ").lower()
        if not user_answer.isalpha():
            print("Numbers or simbols are not allowed. Please try again.")
            time.sleep(1.5)
            continue
        if user_answer == secret_word:
            return True
        else:
            if user_answer in secret_word:
                user_guesses.append(user_answer)
                if masked_word == get_masked_word(secret_word, user_guesses):
                    print("Letter has already been guessed")
                    time.sleep(1.5)
                else:
                    masked_word = get_masked_word(secret_word, user_guesses)
            else:
                if user_answer in user_wrong_answers:
                    print("You have already tried this")
                    time.sleep(1.5)
                else:
                    if total_lives > 1 :
                        print("Sorry, try again!\n")
                        time.sleep(1.5)
                    user_wrong_answers.append(user_answer)
                    total_lives -= 1
        if masked_word == secret_word:
            return True

    return False

def get_valid_input(prompt, valid_options):
    """
    Get a valid input from the user.

    Parameters
    ----------
    prompt : str
        The prompt to be displayed to the user.
    valid_options : list
        A list of valid options the user can input.

    Returns
    -------
    str
        The valid input from the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")
            time.sleep(1.5)
            clear_screen()

def main():
    """
    The main function of the program. It contains the main game loop,
    and handles user input to play again or quit the game.

    The function will randomly select a word from the word_list, and
    then play the game using the play function. If the user wins, it will
    add to the score and print the new score. If the user loses, it
    will print the final score and end the game.

    The function will then ask the user if they want to play again, and
    if the user inputs "n" or "no", it will end the game and print the
    final score. If the user inputs "y" or "yes", it will continue the
    game loop.

    Parameters
    ----------

    None

    Returns
    -------

    None
    """
    keep_going = True
    score = 0

    while keep_going:
        secret_word = random.choice(word_list)

        if play(secret_word):
            clear_screen()
            print(f"You got it!!\n The word was:{secret_word}")
            score += 1
            print(f"Score: {score}")
            time.sleep(1.5)
            clear_screen()
        else:
            clear_screen()
            print(stages[0])
            print(f"You lost!\nThe word you had to guess was: {secret_word}")
            print(f"Score: {score}")
            time.sleep(1.5)
            clear_screen()
  
        play_again = get_valid_input("play again?(y/n): ", ["y", "yes", "n", "no"])
        if play_again.startswith("n"):
            clear_screen()
            print(f"Final score: {score}\nGoodbye!!")
            keep_going = False

if __name__ == "__main__":
    main()