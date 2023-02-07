# Jackson Krieger
# CSCI 101 - Section A
# Python Lab 1A
# References: zyBooks 
# Time: 1 hour


print('Input the numerator of the improper fraction.')
num = int(input('NUMERATOR> '))
print('Input the denominator of the improper fraction.')
den = int(input('DENOMINATOR> '))
x = num // den
y = num % den
print(num, end = '')
print('/', end = '')
print(den, end = '')
print(' as a mixed fraction is:')
print('OUTPUT', x, y, end = '')
print('/', end='')
print(den)



