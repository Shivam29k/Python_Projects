from replit import clear
#word list
from hangman_word import word_list
# word_list = ["aardvark", "baboon", "camel"]

from hangman_art import stages, logo

#generate a random word 
import random
chosen_word = random.choice(word_list)
# print(chosen_word)  #for testing purpose

#create a function to show the blanks
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
# print(display)

#create a function for life count
lives = ["❤️", "❤️", "❤️", "❤️", "❤️","❤️"]
def life_count():
    print('  '.join(lives))
    print("You have", len(lives), "lives left.\n")
    print(stages[len(lives)])

#Is the guessed letter in the word?
def guess_check(letter):
    right_guess = False
    for position in range(word_length):
        if letter == chosen_word[position]:
            display[position] = letter
            right_guess = True
    if right_guess:
        print("\nAyooo You guessed it right !!!\n")
    if not right_guess:
        lives.pop()
        print("\nOoops... Wrong guess !!!\n")

# start of game
print(logo)
gussed_letters = []

while ("_" in display) and (len(lives) != 0):
    life_count()
    print(' '.join(display))

  #ask the user to guess a letter
    guess = input("\nGuess a letter: ").lower()
    clear()
    print(logo)
    if guess in gussed_letters:
      print(f"\nYou have already guessed the letter {guess}\n")
      continue
    guess_check(guess)
    gussed_letters.append(guess)

if "_" not in display:
    print(f"You win. The word was {chosen_word}")
elif len(lives) == 0:
    print(stages[0])
    print("YOU LOSE.")