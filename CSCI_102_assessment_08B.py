# Jackson Krieger
# CSCI 102 - Section A
# Python assessment 08B
# References: Got help from TA Drew and Zach 
# Time: 1 hour

# inputs

print('Enter a DNA string S:')
string = input('S> ')

print('Enter a substring T:')
substring = input('T> ')

# variables

sub_found = 0

indice = 0

num_indices = []

# main code

if len(substring) > len(string):
    print('Error: Substring is longer than DNA string')
    print('OUTPUT ERROR')

# find indices first and use indices count for total number found

while indice <= len(string):

    indice = string.find(substring, indice)

    if indice < 0:
        break
    num_indices.append(str(indice))
    indice += 1   
    sub_found = len(num_indices)

print(f'The total number of substrings found is {sub_found}')
print(f'OUTPUT {sub_found}')
print(f'The starting indices of these substrings in S are: {" ".join(num_indices)}')
print(f'OUTPUT {" ".join(num_indices)}')
