# Jackson Krieger
# CSCI 101 - Section A
# Python lab 3
# References: TA Drew helped figure out why my outputs were wrong
# Time: 1 hour

size = int(input('SIZE> '))

if size == 3:

    row0 = input('ROW0> ')
    row1 = input('ROW1> ')
    row2 = input('ROW2> ')

    string0 = row0[:]
    string1 = row1[:]
    string2 = row2[:]


# if inputs are not 3 for each row
    if len(string0) != 3:
        print('OUTPUT ERROR')

    elif len(string1) != 3:
        print('OUTPUT ERROR')

    elif len(string2) != 3:
        print('OUTPUT ERROR')

# horizontal wins for X
    elif row0 == 'XXX':
        print('OUTPUT X')

    elif row1 == 'XXX':
        print('OUTPUT X')

    elif row2 == 'XXX':
        print('OUTPUT X')

# horizontal wins for O
    elif row0 == 'OOO':
        print('OUTPUT O')

    elif row1 == 'OOO':
        print('OUTPUT O')

    elif row2 == 'OOO':
        print('OUTPUT O')

# diagonal and vertical wins for X
    elif string0[0] == 'X' and string1[0] =='X' and string2[0] == 'X':
        print('OUTPUT X')

    elif string0[1] == 'X' and string1[1] == 'X' and string2[1] == 'X':
        print('OUTPUT X')

    elif string0[2] == 'X' and string1[2] == 'X' and string2[2] == 'X':
        print('OUTPUT X')

    elif string0[0] == 'X' and string1[1] == 'X' and string2[2] == 'X':
        print('OUTPUT X')

    elif string0[2] == 'X' and string1[1] == 'X' and string2[0] == 'X':
        print('OUTPUT X')

# diagonal and vertical wins for O
    elif string0[0] == 'O' and string1[0] == 'O' and string2[0] == 'O':
        print('OUTPUT O')

    elif string0[1] == 'O' and string1[1] == 'O' and string2[1] == 'O':
        print('OUTPUT O')

    elif string0[2] == 'O' and string1[2] == 'O' and string2[2] == 'O':
        print('OUTPUT O')

    elif string0[0] == 'O' and string1[1] == 'O' and string2[2] == 'O':
        print('OUTPUT O')

    elif string0[2] == 'O' and string1[1] == 'O' and string2[0] == 'O':
        print('OUTPUT O')

# if rows do not contain X, O, or E
    elif 'X' not in string0 and 'E' not in string0 and 'O' not in string0:
        print('OUTPUT ERROR')

    elif 'X' not in string1 and 'E' not in string1 and 'O' not in string1:
        print('OUTPUT ERROR')

    elif 'X' not in string2 and 'E' not in string2 and 'O' not in string2:
        print('OUTPUT ERROR')

# if there are no winners
    else:
        print('OUTPUT N')

if size == 4:

    row0 = input('ROW0> ')
    row1 = input('ROW1> ')
    row2 = input('ROW2> ')
    row3 = input('ROW3> ')

    string0 = row0[:]
    string1 = row1[:]
    string2 = row2[:]
    string3 = row3[:]
        
# if inputs are not 4 for each row
    if len(string0) != 4:
        print('OUTPUT ERROR')

    elif len(string1) != 4:
        print('OUTPUT ERROR')
    
    elif len(string2) != 4:
        print('OUTPUT ERROR')

# horizontal wins for X
    elif row0 == 'XXXX':
        print('OUTPUT X')

    elif row1 == 'XXXX':
        print('OUTPUT X')

    elif row2 == 'XXXX':
        print('OUTPUT X')

    elif row3 == 'XXXX':
        print('OUTPUT X')

# horizontal wins for O
    elif row0 == 'OOOO':
        print('OUTPUT O')

    elif row1 == 'OOOO':
        print('OUTPUT O')

    elif row2 == 'OOOO':
        print('OUTPUT O')

    elif row3 == 'OOOO':
        print('OUTPUT O')

# diagonal and vertical wins for X
    elif string0[0] == 'X' and string1[0] =='X' and string2[0] == 'X' and string3[0] == 'X':
        print('OUTPUT X')

    elif string0[1] == 'X' and string1[1] == 'X' and string2[1] == 'X' and string3[1] == 'X':
        print('OUTPUT X')

    elif string0[2] == 'X' and string1[2] == 'X' and string2[2] == 'X' and string3[2] == 'X':
        print('OUTPUT X')

    elif string0[3] == 'X' and string1[3] == 'X' and string2[3] == 'X' and string3[3] == 'X':
        print('OUTPUT X')

    elif string0[0] == 'X' and string1[1] == 'X' and string2[2] == 'X' and string3[3] == 'X':
        print('OUTPUT X')

    elif string0[3] == 'X' and string1[2] == 'X' and string2[1] == 'X' and string3[0] == 'X':
        print('OUTPUT X')

# diagonal and vertical wins for O
    elif string0[0] == 'O' and string1[0] == 'O' and string2[0] == 'O' and string3[0] == 'O':
        print('OUTPUT O')

    elif string0[1] == 'O' and string1[1] == 'O' and string2[1] == 'O' and string3[1] == 'O':
        print('OUTPUT O')

    elif string0[2] == 'O' and string1[2] == 'O' and string2[2] == 'O' and string3[2] == 'O':
        print('OUTPUT O')

    elif string0[3] == 'O' and string1[3] == 'O' and string2[3] == 'O' and string3[3] == 'O':
        print('OUTPUT O')

    elif string0[0] == 'O' and string1[1] == 'O' and string2[2] == 'O' and string3[3] == 'O':
        print('OUTPUT O')

    elif string0[3] == 'O' and string1[2] == 'O' and string2[1] == 'O' and string3[0] == 'O':
        print('OUTPUT O')

# if rows do not contain X, O, or E
    elif 'X' not in string0 and 'E' not in string0 and 'O' not in string0:
        print('OUTPUT ERROR')

    elif 'X' not in string1 and 'E' not in string1 and 'O' not in string1:
        print('OUTPUT ERROR')

    elif 'X' not in string2 and 'E' not in string2 and 'O' not in string2:
        print('OUTPUT ERROR')

    elif 'X' not in string3 and 'E' not in string3 and 'O' not in string3:
        print('OUTPUT ERROR')

# if there are no winners
    else:
        print('OUTPUT N')

