#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 05B
#   References: TA Drew helped with figuring out what the math was
#   Time: 1 hour


# input statements
print("Enter number of empty bottles in Blaster's possession at the start of the day.")
empties = int(input('EMPTIES> '))

print('Enter the number of empty bottles that Blaster found during the day.')
found = int(input('FOUND> '))

print('Enter the number of empty soda bottles required to buy a new soda.')
cost = int(input('COST> '))

# variables for equations
total = empties + found

leftover = total % cost

drank = 0


# while loop for calculating sodas drank
while total // cost > 0:
    if total % cost == 0:
        drank += total // cost
        total = total // cost
# else statement for adding sodas with remainders
    else: 
        drank += total // cost
        leftover = total % cost
        total = total // cost + leftover

# final print statement
print('The total number of sodas that Blaster drank is:')
print(f'OUTPUT {int(drank)}')

    
