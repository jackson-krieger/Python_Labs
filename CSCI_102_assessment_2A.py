
# Jackson Krieger
# CSCI 102 - Section A
# Time 20 minutes


print('Input the first operand.')
operand_one = float(input('FIRST> '))
print('Input the second operand.')
operand_two = float(input('SECOND> '))


var_sum = operand_one + operand_two
var_dif = operand_one - operand_two
var_quotient = operand_one // operand_two
var_product = operand_one * operand_two
var_remainder = operand_one % operand_two

print(f'The sum of {operand_one} and {operand_two} is {var_sum:.1f}.')
print(f'OUTPUT {var_sum:.1f}')
print(f'The difference of {operand_one} and {operand_two} is {var_dif:.1f}.')
print(f'OUTPUT {var_dif:.1f}')
print(f'The product of {operand_one} and {operand_two} is {var_product:.1f}.')
print(f'OUTPUT {var_product:.1f}')
print(f'The sum of {operand_one} and {operand_two} is {var_quotient:.0f}.')
print(f'OUTPUT {var_quotient:.0f}')
print(f'The remainder of {operand_one} and {operand_two} is {var_remainder:.2f}.')
print(f'OUTPUT {var_remainder:.2f}')
