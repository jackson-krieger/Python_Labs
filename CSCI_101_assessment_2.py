# Jackson Krieger
# CSCI 101 - Section A
# Python assessment 2
# References: Went to office hours to get help and emailed professor for help with why some tests were failing
# Time: 2 hours

print('Welcome to the Binary-Decimal-Hex Converter')
print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

print('Enter an option:')
print('1. Binary-Decimal Conversion')
print('2. Decimal-Binary Conversion')
print('3. Hexadecimal-Decimal Conversion')
print('4. Decimal-Hexadecimal Conversion')

option = int(input('OPTION> '))

# for binary to decimal

bin_string_input = 0

check = True

# for decimal to binary string

decimal = 0

string = 0

string2 = 0

remainder = []

final = 0


# binary to decimal

if option == 1:
    bin_string_input = str(input('BINARY-STR> '))
    for i in bin_string_input:
        if i.isalpha() or int(i) > 1:
            print(f'{bin_string_input} is not a Binary number')
            print('OUTPUT ERROR')
            check = False
            break
    if check == True:
        r = list(reversed(bin_string_input))
        for i in range(len(r)):
            if r[i] == '1':
                decimal += 2 ** i
        print(f'Binary {bin_string_input} is Decimal {decimal}')
        print(f'OUTPUT {decimal}')

    
# decimal to binary

if option == 2:
    string = str(input('DECIMAL-STR> '))
    decimal = string
    for i in string:
        if i.isalpha():
            print(f'{decimal} is not a Decimal number')
            print('OUTPUT ERROR')
            check = False
            break
    if check == True:
        decimal = int(string)
        if decimal == 0:
            print('Decimal 0 is Binary 0')
            print('OUTPUT 0')
        elif decimal > 0:
            while decimal > 0:
                string2 = int(decimal % 2)
                decimal = int(decimal / 2)  
                remainder.append(str(string2))
            r = list(reversed(remainder))
            final = ''.join(r)
            print(f'Decimal {string} is Binary {final}')
            print(f'OUTPUT {final}')
