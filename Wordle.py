import random
import sys 
from termcolor import colored
import nltk
nltk.download('words')
from nltk.corpus import words

def user_input():
    print("Welcome to Wordle!")
    print("Guess a 5 letter word")
#user_input()
def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words)
#word = read_random_word()
#print(word)

def nltk_generate_random_word():
    pass

nltk.data.path.append('/word/words')
word_list = words.words()
five_letter_words = [word for word in word_list if len(word) == 5]

play_again = ""
while play_again != 'q':
    user_input()
    #word = read_random_word()
    word = random.choice(five_letter_words)
    for attempt in range(1,7):
        guess = input().lower()
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(colored(guess[i], 'grey'), end="")
        print()
        if guess == word:
            print(colored(f"Congrats! You got the wordle in {attempt} gusses", 'blue'))
            break
        elif attempt == 6:
            print(colored(f"Sorry, the wordle was {word}", 'red'))
        print()
    play_again = input("Want to play again? Type q to exit ")