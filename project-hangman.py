#hang man project
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives=6
words = ['believe','the','things','say','about','when','drunk','distance','leaves','bitter','taste']
word = random.choice(words)
print("Welcome to hangman!")
print("Guess this word")
# for i in word:
#     print('_',end="")
choices=""
f=1
print("\n")
guess=""
while(f and lives): #f incase the user guessed it before losing all lives
    for i in word:
        if (i == guess.lower() or i in choices):
            print(f"{i}", end='')
        else:
            print("_", end='')
    guess = input("\nEnter the character: ")
    if(guess in choices):
        if guess in word:
            print(f"You've already guessed {guess}")
        else:
            print(f"You've already lost a life guessing {guess}.Try another character")
    elif(guess not in word):
        print("Oops! the character is not present in the word")
        lives -= 1
        print(stages[lives])
        print(f"You guessed '{guess}' which is not present in the word. You lost a life.")
        print(f"Just so you know, {lives} chances are left to guess the word") if lives else print("You're out of lives :( ")
    else:
        print(f"You guessed it correctly, the character {guess} is present in the word")
        #choices=choices+guess
    choices = choices + guess
    f = 0
    for i in word:
        if (i not in choices):
            f = 1
if(lives!=0):
    print("\nYou win!")
else:
    print("\nMeet you in the next game")
