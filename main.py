import random
#prints Hangman logo
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      ''')
#an empty list for the chosen word
display = []
from pathlib import Path
#create a list of words for the game from a text file
filepath = Path('wordlist')
word_list = filepath.read_text().splitlines()
#randomly choose a word from list of words
chosen_word = random.choice(word_list)
#hangman ascii arts
hangman = '''           +---+
           |   |
               |
               |
               |
               |
         ========='''
hangman1 = '''           +---+
           |   |
           O   |
               |
               |
               |
         ========='''
hangman2 = '''           +---+
           |   |
           O   |
           |   |
               |
               |
         ========='''
hangman3 = '''           +---+
           |   |
           O   |
          /|   |
               |
               |
         ========='''
hangman4 = '''           +---+
           |   |
           O   |
          /|\  |
               |
               |
         ========='''
hangman5 = '''           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
         ========='''
hangman6 = '''           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
         ========='''
print(hangman)
#hangman ascii arts in a list
hangman_list = [
    hangman, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6
]
print("\n\n")
#print blanks with same length as chosen word
for x in range(0, len(chosen_word)):
    display.append("_")
print(display)
life = 0
while (life < 6):
#ask user to enter a letter
    guess = input("\n\nGuess a letter: ").lower()
#if letter is not found in word, increment life by one and print hangman art; if it is found, print blanks with correct letter
    for x in range(0, len(chosen_word)):
        if guess not in chosen_word:
            print(hangman_list[life + 1])
            life += 1
            break
        if guess == chosen_word[x]:
            display[x] = chosen_word[x]
            

    if guess in chosen_word:
        print(hangman_list[life])

    print(f"\n\n{display}")
    print("\n---------------------------------------------------------------")
    if life == 6:
        print("\nSorry, you lost :(")
        print(f"The word was {chosen_word}")
        exit

    if ''.join(display) == chosen_word:
        print("\n YOU WON!!!")
        break
