"""
File: word_guess.py
-------------------
Fill in this comment.
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    HIDDEN_SECRET_WORD = '-' * len(secret_word)
    CHANCE_GUESSES = INITIAL_GUESSES
    PAST_GUESSES = ''

    while HIDDEN_SECRET_WORD != secret_word and CHANCE_GUESSES != 0:
        print(f'The word now looks like this: {HIDDEN_SECRET_WORD}')
        if CHANCE_GUESSES > 1:
            print(f'You have {CHANCE_GUESSES} guesses left.')
        elif CHANCE_GUESSES == 1:
            print(f'You have {CHANCE_GUESSES} guess left.')

        if PAST_GUESSES != '':
            print(f'Your past guesses are {PAST_GUESSES}.')

        LETTER = input('Type a single letter here, then press enter:').upper()

        if len(LETTER) == 1 and LETTER in secret_word: # right single letter
            PAST_GUESSES += LETTER
            for i in range(len(secret_word)):
                if secret_word[i] == LETTER:
                    HIDDEN_SECRET_WORD = HIDDEN_SECRET_WORD[:i] + LETTER + HIDDEN_SECRET_WORD[i+1:]
            print('That guess is correct.')
            if HIDDEN_SECRET_WORD != secret_word:
                print()
        elif len(LETTER) == 1 and LETTER not in secret_word: # wrong single letter
            CHANCE_GUESSES -= 1
            PAST_GUESSES += LETTER
            print(f"There are not {LETTER}'s in the word.")
            if CHANCE_GUESSES != 0:
                print()
        else: # not single letter
            print('A guess should be a single character.' + '\n')

    if HIDDEN_SECRET_WORD == secret_word: # win
        print(f'Congratulations, the word is: {secret_word}')
    else: # lose
        print(f'Sorry, you lost. The secret word was: {secret_word}')


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    all_word_with_newline = open(LEXICON_FILE).readlines()
    all_word = [word.strip() for word in all_word_with_newline]
    index = random.randrange(len(all_word))
    return all_word[index]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()