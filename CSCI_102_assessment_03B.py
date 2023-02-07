# Jackson Krieger
# CSCI 102 - Section A
# Python lab 03B
# References: none
# Time: 30 minutes

print('Welcome to our Enhanced Calculator!')

print('Input the first operand.')
operand_one = float(input('FIRST> '))

print('Input the second operand')
operand_two = float(input('SECOND> '))

addition = operand_one + operand_two
subtraction = operand_one - operand_two
multiplication = operand_one * operand_two
quotient = operand_one // operand_two
remainder = operand_one % operand_two

print('Choose one of the following operations')
print('1 - addition')
print('2 - subtraction')
print('3 - multiplication')
print('4 - division')

operation = int(input('OPERATION> '))

if operation == 1:
    print(f'The result of the addition is: {addition:.6f}')
    print(f'OUTPUT {addition:.6f}')

elif operation == 2:
    print(f'The result of the subtraction is: {subtraction:.6f}')
    print(f'OUTPUT {subtraction:.6f}')

elif operation == 3:
    print(f'The result of the multipication is: {multiplication:.6f}')
    print(f'OUTPUT {multiplication:.6f}')

elif operation == 4:
    print(f'The result of the division is: {int(quotient)} (quotient) and {int(remainder)} (remainder)')
    print(f'OUTPUT {int(quotient)}')
    print(f'OUTPUT {int(remainder)}')

else:
    print('Invalid input')

print('Thank you for using our calculator')

