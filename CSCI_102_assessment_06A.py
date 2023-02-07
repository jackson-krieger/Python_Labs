# Jackson Krieger
# CSCI 101 - Section A
# Python Lab 6A
# References: none
# Time: 30 minutes


# number input
print('Enter the number to create multiples for.')
num = int(input('NUMBER> '))

# index max
print('Enter the maximum index of the list')
index_max = int(input('INDEX> '))

# variables
num_list = []

multiple = 0

r = 0

# while loop to calculate multiples
while r <= index_max:
    multiple = num * (r + 1)
    r = r + 1
    num_list.append(multiple)


print('Your list of multiples is as follows:')
print(f'OUTPUT {num_list}')

print('The first multiple calculated is:')
print(f'OUTPUT {num}')
          
