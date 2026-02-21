from hangman_words_real import words as word_list
from hangman_art import logo, stages
import random
import os
import time

def get_masked_word(x : str, y : str):
    """Return a string where each character in x is replaced with '_' if it is not in y.

    Parameters:
    x (str): The string to be masked.
    y (str): The string containing the characters to be kept.

    Returns:
        str: The masked string.
    """
    return "".join([p if p in y else "_" for p in x])

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

keep_going = True
score = 0


while keep_going:
    secret_word = random.choice(word_list)
    user_guesses = []
    user_wrong_answers = []
    masked_word = get_masked_word(secret_word, user_guesses)
    total_lives = 6

    while masked_word != secret_word and total_lives > 0:
        clear_screen()
        print(logo)
        print(stages[total_lives])
        # print(secret_word) #for test
        print(f'''Guess a letter of the word:
                {get_masked_word(secret_word, user_guesses)}''')
        user_answer = input(f"you have {total_lives} attempts left: ").lower()
        if user_answer == secret_word: #If the player guesses right away" or "In case the user guesses immediately
            score += 1
            masked_word = secret_word
        else:
            if user_answer in secret_word:
                user_guesses.append(user_answer)
                if masked_word == get_masked_word(secret_word, user_guesses):
                    print("Letter has already been guessed")
                else:
                    masked_word = get_masked_word(secret_word, user_guesses)
                    print(masked_word)
                    score += 1
            else:
                if user_answer in user_wrong_answers:
                    print("You have already tried this")
                    time.sleep(1)
                else:
                    if total_lives > 1 :
                        print("Sorry, try again!\n")
                        time.sleep(1)
                    user_wrong_answers.append(user_answer)
                    total_lives -= 1

    if total_lives > 0:
        print("You got it!!")
    else:
        clear_screen()
        print(logo)
        print(stages[total_lives])
        print(f"You lost!\nThe word you had to guess was: {secret_word}")
        
    play_stop = input("'C'ontinue 'S'top: ").lower()
    if play_stop == "c":
        clear_screen()
        print(logo)
        continue
    elif play_stop == "s":
        clear_screen()
        print(logo)
        print(f"Score= {score}\nGoodbye!!")
        keep_going = False
        
