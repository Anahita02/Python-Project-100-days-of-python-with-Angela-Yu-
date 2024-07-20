#Hangman project

import random
from hangman_words import word_list
from hangman_ascii import stages

chosen_word = random.choice(word_list)

lives = 6

print(f"Pssst, the solution is {chosen_word}")

display = []

for letter in chosen_word:
  display+= "-"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed leter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
         print(f"You guessd {guess}, that's not in the word. You lose a life.")
         lives -= 1
         if lives == 0:
             end_of_game = True
             print("You lose!")
    print(f"{' '.join(display)}")
    if "-" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])