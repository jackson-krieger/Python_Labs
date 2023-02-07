# Jackson Krieger
# CSCI 102 section A
# Python assessment 09
# References: Went to office hours
# Time: 30 minutes


# variables
import random

word_list = []

# open file for read
with open('dictionary.txt', 'r') as f:
    print('Enter the length of the words to find')
    word_length = int(input('LENGTH> '))
    print('Enter the seed to use:')
    seed_val = input('SEED> ')
    random.seed(seed_val)
    blank_list = f.read().splitlines()

    # for loop appending everything to a list
    for i in blank_list:
        if len(i) == word_length:
            word_list.append(i)

index = random.randint(0, len(word_list))

# outputs
print(f'The number of words with length {word_length} is:')
print(f'OUTPUT {len(word_list)}')
if len(word_list) == 0:
    print(f'There are no words of length {word_length} in the dictionary:')
    print('OUTPUT None')
if len(word_list) == 1:
    print(f'Here is the only word with length {word_length}:')
    print(f'OUTPUT {word_list[index]}')
if len(word_list) != 0:
    print(f'Here is a random word with length {word_length}:')
    print(f'OUTPUT {word_list[index]}')
