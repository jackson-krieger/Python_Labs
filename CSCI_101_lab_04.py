# Jackson Krieger
# CSCI 101 - Section A
# Python lab 4
# References: None
# Time: 2 hours

import random
print("Welcome to Wordle!")
print("Here you will provide the length of the words you want to play with and")
print("a random seed value to start the game!")
valid_lengths = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                 15, 16, 17, 18, 19, 20, 21, 22, 24, 28, 29]

length_is_valid = False
while not length_is_valid:
    word_length = int(input('LENGTH> '))

    if word_length in valid_lengths:
        length_is_valid = True
    else:
        print(f"There are no {word_length}-letter words in the game.")
        print("Please pick again.")

seed = input('SEED> ')
word_bank = []

with open("dictionary.txt", 'r', encoding='utf-8') as dictionary_file:
    for line in dictionary_file:
        line = line.strip()
        if len(line) == word_length:
            word_bank.append(line)

random.seed(seed)
secret_word = random.choice(word_bank)
num_guesses_allowed = 6
num_guesses_used = 0
game_result = ""
guess_list = []

while game_result == "":
    
    guess_is_valid = False
    
    while not guess_is_valid:
        new_guess = input("GUESS> ")
        new_guess = new_guess.lower()
        
        if len(new_guess) != word_length:
            print(f"Please enter a {word_length}-letter word.")

        elif new_guess not in word_bank:
            print(f"Please enter a real word.")

        elif new_guess in guess_list:
            print(f"Please enter a word you haven't guessed yet.")

        else:
            guess_is_valid = True


    result_list = list('_' * word_length)

    secret_list = list(secret_word)

    for i in range(0,len(new_guess)):
        if new_guess[i] == secret_list[i]:
            result_list[i] = "x"
            secret_list[i] = "_"

    for i in range(0,len(new_guess)):
        if result_list[i]== "x":
            continue
        else:
            for j in range(0,len(secret_list)):
                if new_guess[i]==secret_list[j]:
                    result_list[i] = "o"
                    secret_list[j] = "_"
                    break

    print(f"OUTPUT {' '.join(result_list)}")
    guess_list.append(new_guess)
    num_guesses_used += 1
    temp = 0
    for i in range(0,len(result_list)):
        if result_list[i] == "x":
            temp+=1
    if(temp == len(result_list)):
        game_result = "Won"
    elif(num_guesses_used == num_guesses_allowed):
        game_result = "Lost"

print("Game over.")

if game_result == "Won":
    print(f"Congratulations!")
    print(f"You guessed the word '{secret_word}' in {num_guesses_used} guesses!")
    print("You win!")
elif game_result == "Lost":
    print(f"You were not able to guess the word '{secret_word}'.")
    print("You lose.")

print(f"OUTPUT {secret_word}")
print(f"OUTPUT {game_result}")
