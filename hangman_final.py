import random
import os

def clear_console():
    os.system('cls')

def get_guess() -> str:
    guess = ""
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Guess a letter:").lower()
    return guess

def display_blanks(display:list):
    for letter in display:
        print(letter, end=" ")
    print("")

logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

clear_console()
print(logo)
user_input = input("Ready? Y/N ")
while user_input.upper() == "Y":
    ended = False
    lives = 6
    guesses = []
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    display = []
    for _ in range(word_length):
        display += "_"
    print(hangman_pics[0])
    
    while not ended:
        display_blanks(display)
        guess = get_guess()
        if guess in guesses:
            print("You already used this guess")
        elif guess not in chosen_word:
            lives -= 1
            print(hangman_pics[-(lives + 1)])
        else:
            for index in range(len(chosen_word)):
                if chosen_word[index] == guess:
                    display[index] = guess
        if guess not in guesses:
            guesses += guess
        ended = True if lives == 0 or "_" not in display else False

    if (lives == 0):
        print("Game over")
    else:
        print("You won!")
    print(f"The correct word was: {chosen_word}")
    user_input = input("Start again? Y/N ")
print("Thanks for playing! See you soon!")
        
    


