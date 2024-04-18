import random
from hangman import update_hangman, hangman_image
from hangman_words import word_list

word = random.choice(word_list)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = []
blank_word = []

lives = 6

# split word to list of characters
for c in word:
    chosen_word.append(c)

# replace characters in word with _
for c in chosen_word:
    blank_word.append('_')

while lives > 0 and '_' in blank_word:

    for h in hangman_image:
        print(''.join(h))

    print('\n')
    # print(f'\nYou have {lives} lives\n')
    print(' '.join(blank_word))

    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called          guess. Make guess lowercase.
    user_input = input('\nGuess a letter:\n').lower()

    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the            chosen_word.
    if user_input in chosen_word:
        print('Right\n')
        for i in chosen_word:
            if user_input == i:
                index = chosen_word.index(user_input)
                chosen_word[index] = '_'
                blank_word[index] = i
    else:
        print(
            f"You guessed {user_input}, that's not in the word. You lose a life."
        )
        lives -= 1
        update_hangman(lives)

    print('-------------------------------------------------------\n')

if lives > 0:

    print('You WON')
else:
    print(f'The word was {word}')
    print('You Lose')
