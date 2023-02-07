# Jackson Krieger
# CSCI 101 - Section A
# Python lab 1
# References: none
# Time: 10 minutes

print('Enter your string.')

string = input('STRING> ')

print('Enter four numbers to slice the string')

a = int(input('A> '))
b= int(input('B> '))
c = int(input('C> '))
d = int(input('D> '))

string_one = string[a+ 1 : b]
string_two = string[c + 1 : d]
output = string_one + " " + string_two
print(f'OUTPUT {output}')

        
