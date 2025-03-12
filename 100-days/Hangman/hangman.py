import random
import hangman_words
import hangman_art


# TODO-1 - Randomly choose a word from the word_list and assign it to a a variable called chosen_word

chosen_word = random.choice(hangman_words.animals).lower()

place_holder = "_" * len(chosen_word)
life_count = 5

print(hangman_art.intro)
print(place_holder)

incorrect_letter =[]
correct_letter = []

# TODO-2 - Ask the user to guess a letter and assign the answer to a variable called guess
while place_holder != chosen_word and life_count > 0:

    guess = input("Guess a letter:").lower()

        # TODO-3 -  Check if the letter the user guessed is in one of the chosen letters in the chosen_word. print Rigth if it is wrong if not
    if guess in chosen_word:
        chosen_list = list(place_holder)
        for index,letter in enumerate(chosen_word):
            if guess == letter:
                chosen_list[index] = letter

        place_holder = ''.join(chosen_list)
        print(place_holder)


    else:
        life_count -= 1
        incorrect_letter.append(guess)
        print(f"You lost 1 life; Remaining lives: {life_count}")
        print(hangman_art.hangman_stages[life_count])


if place_holder == chosen_word:
    print("You won madafaka! 🎉")
else:
    print(f"You lost! The word was: {chosen_word}")