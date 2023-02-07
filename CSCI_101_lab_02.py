# Jackson Krieger
# CSCI 101 - Section A
# Python lab 2
# References: Worked with Tyner Sellers
# Time: 1 hour

print('Input the five lists of characters to be encrypted.')

list_one = input('LIST1> ')
list_two = input('LIST2> ')
list_three = input('LIST3> ')
list_four = input('LIST4> ')       
list_five = input('LIST5> ')
half_three = int(len(list_three) / 2)

encrypted = f'{list_five[0:2]} {list_one[-2:]}{list_one[:-2]}{list_two[:-2]}{list_three[-half_three:]}{list_four[0:2]}{list_four[4]}{list_four[3]}{list_four[2]}{list_four[5:]} {list_five[2:]}'

print('The encrypted message is:')
print('OUTPUT', encrypted)
