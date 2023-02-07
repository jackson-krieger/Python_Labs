#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 05A
#   References: ZyBooks to help with appending to list and getting sum of list
#   Time: 30 minutes

print('Enter values to add. Enter quit when done.')

value_sum = 0

value_string = []
while True:
    value_input = input('NUMBER> ')
    if value_input != 'quit':
        value_string.append(value_input)
    else:
        break

length = len(value_string)

for value in range(length):
    value_sum = value_sum + int(value_string[value])

print(f'The addition of the {length} numbers entered is:')
print(f'OUTPUT {length} numbers')
print(f'OUTPUT {value_sum} total')
