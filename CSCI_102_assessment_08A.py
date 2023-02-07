# Jackson Krieger
# CSCI 102 - Section A
# Python assessment 08A
# References: zybooks and posted youtube video
# Time: 30 minutes

# inputs

print('Input the seed for the random number generator:')
seed = int(input('SEED> '))

print('Input the number of sides of the die:')
sides = int(input('SIDES> '))

print('Input the number of rolls to make:')
rolls = int(input('ROLLS> '))

# variables
import random

random.seed(seed)

num_list = []

# for loop

for num in range(0, rolls):
    rand_num = random.randint(1, sides)
    num_list.append(rand_num)


i = 1

print(f'Your {rolls} rolls of a {sides}-sided die follow:')

for number in range(0, sides):
    count = num_list.count(i)
    print(f'OUTPUT {i} occurred {count} times')
    i += 1

            
           
