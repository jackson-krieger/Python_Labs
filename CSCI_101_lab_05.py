# Jackson Krieger
# CSCI 101 - Section A
# Python lab 5
# References: 
# Time:


# initial statement

print('Input the number of rows and columns in the subdivision:')
rows = int(input('ROWS> '))
columns = int(input('COLUMNS> '))

# variables

i = 0
j = 0
k = 0
row_list = []
column_list = []
total_list = []
final_list = []
charge = True
charge1 = True
charge2 = True
charge3 = True
charge4 = True
charge5 = True
charge6 = True
charge7 = True

# for loop for row inputs

print('Input each row of the subdivision.')
for i in range(rows):
    row = input(f'ROW{i}> ')
    row = row.split(' ')
    
    total_list.append(row)

for i in range(rows):
    for j in range(columns):
        if i < rows and j < columns and total_list[i][j] == 'b':
            if i < rows - 1:
                if total_list[i+1][j] != 'T':
                    charge = False
            if j < columns - 1:
                if total_list[i][j+1] != 'T':
                    charge1 = False
            if j < columns - 1 and i < rows - 1:
                if total_list[i + 1][j + 1] != 'T':
                    charge2 = False
            if charge == False and charge1 == False and charge2 == False:
                final_list.append([i,j])
            if i < rows - 1:
                if total_list[i+1][j] == 'T':
                    charge = True
            if j < columns - 1:
                if total_list[i][j+1] == 'T':
                    charge1 = True
            if j < columns - 1 and i < rows - 1:
                if total_list[i + 1][j + 1] == 'T':
                    charge2 = True
            if charge == True and charge1 == True and charge2 == True:
                final_list.append([i,j])
print(final_list)

# need 8 boolean variables. charge right, left, up, down, diagonal
