# Jackson Krieger
# CSCI 101 - Section A
# Python Assessment 7
# References: Went to office hours
# Time:  minutes

print('How many rows does the chessboard have?')
rows = int(input('ROWS> '))

print('How many columns does the chessboard have?')
columns = int(input('COLUMNS> '))

print('What are the strings with which to pattern it?')
first = input('FIRST> ')
second = input('SECOND> ')

# variables
column_count = 0
row_count = 0
board_list = []
array_list = []
final_list = []

# print statement
print(f'A chessboard with {rows} rows, {columns} columns, first string is {first}, and second string is {second} is:')

# while loop for column count
while column_count < columns: 
    board_list.append(first)
    column_count += 1
    if column_count == columns:
        break
    board_list.append(second)
    column_count += 1
    
# if columns are odd
for i in board_list:
    if i == first:
        array_list.append(second)
    elif i == second:
        array_list.append(first)
    
# while loop for row count
while row_count < rows:
    print(f'OUTPUT {board_list}')
    final_list.append(board_list)
    row_count += 1
    if row_count == rows:
        break
    print(f'OUTPUT {array_list}')
    final_list.append(array_list)
    row_count += 1

# final output
print('And the 2D array representation is:')
print(f'OUTPUT {final_list}')
