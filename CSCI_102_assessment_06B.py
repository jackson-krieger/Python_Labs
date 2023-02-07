# Jackson Krieger, Rebecca Brown, Grey Garner, Thomas Rinbey
# CSCI 102 - Section A
# Python Lab 6B
# References: Went to office hours
# Time: 15 minutes


# inputs
print('Count of numbers to estimate')
count = int(input('COUNT> '))

value_list = []

# input print for list numbers
print('Input each number to estimate')

# for loop that prints number inputs
for i in range(count):
    value_list.append(float(input('NUMBER> ')))

# for loop that runs while loop
for num in value_list:

    initial_guess = 10

    better_guess =  (initial_guess + num / initial_guess) / 2

    iteration = 1

# while loop that runs however many times needed to estimate the square root
    while initial_guess != better_guess:
        initial_guess = better_guess
        better_guess = (initial_guess + num / initial_guess) / 2
        iteration += 1
    # output
    print('The square roots are as follows:')
    print(f'OUTPUT After {iteration} iterations, {num}^0.5 = {better_guess:.2f}')
                        
