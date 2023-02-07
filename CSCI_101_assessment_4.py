# Jackson Krieger
# CSCI 101 - Section A
# Python Assessment 4
# References: TA Drew
# Time: 2 hours

import csv

# Make sure to follow the provided instructions for each of the steps on Canvas!

# Step 1: Month based stats
def monthly_summary(filename, month_abbr):
    with open (filename, 'r', encoding='utf-8') as file:
        read = csv.reader(file)
        var = []
        for i in read:
            if month_abbr in i:
                ind = i.index(month_abbr)
            else:
                for x in range(len(i)):
                    min_val = i[0]
                    if x == ind:
                        
                        var.append(float(i[x]))
    print('OUTPUT Average: ' + str(round(sum(var) / len(var))) + ' | Minimum: ' + str(round(min(var))) + ' | Maximum: ' + str(round(max(var))))
    

# Step 2: City based stats
def city_summary(filename, city, country):
    with open (filename, 'r', encoding='utf-8') as file:
        read = csv.reader(file)
        var = []
        for i in read:
            if i[0] == country:
                if i[1] == city:
                    vowel = i[2:]
                    for i in vowel:
                        c = float(i)
                        var.append(c)
    print('OUTPUT Average: ' + str(round(sum(var) / len(var))) + ' | Minimum: ' + str(round(min(var))) + ' | Maximum: ' + str(round(max(var))))
                        
            
        
        
            

# Step 3: Sunshine threshold
def cities_in_range(filename, minimum, maximum):
    with open (filename, 'r', encoding='utf-8') as file:

        if maximum != 'None':
            maximum = float(maximum)
        if maximum == 'None':
            maximum = 100000000
        if minimum != 'None':
            minimum = float(minimum)
        if minimum == 'None':
            minimum = 0.0
        read = csv.reader(file)
        var = []
        var2 = []
        for i in read:
            if 'Jan' not in i[2:]:
                for x in i[2:]:
                    c = float(x)
                    var2.append(c)
            if sum(var2) >= minimum and sum(var2) <= maximum:
                var.append(i[1] + ', ' + i[0])
            var2 = []
        return(f'OUTPUT {var}')
                    

# Extra credit: Validating your input file
def valid_csv(filename):
    pass # placeholder line - delete before writing code here

# Step 4: Tying it all together



if __name__ == "__main__":
    print('Here comes the sun!')
    print('Provide the name of your csv file containing sunshine duration data')
    name = input('FILENAME> ')
    print('--------------------------------------------')

    choice = input('CHOICE> ')
    while (choice == '1') or (choice == '2') or (choice == '3'):
        if choice == '1':
            print('Enter the month abbreviation')
            month = input('MONTH> ')
            monthly_summary(name, month)

        if choice == '2':
            print("Enter the city's name")
            city = input('CITY> ')
            print("Enter the country's name")
            country = input('COUNTRY> ')
            city_summary(name, city, country)
        
        if choice == '3':
            print('Enter the minimum amount (in hours) of yearly sunshine')
            minimum = input('MIN> ')
            print('Enter the maximum amount (in hours) of yearly sunshine')
            maximum = input('MAX> ')
            print(cities_in_range(name, minimum, maximum))
        print('--------------------------------------------')
        choice = input('CHOICE> ')
    print("Goodbye!")

    
                        
    # You MUST write your code for Step 4 here (inside the if-statement)
