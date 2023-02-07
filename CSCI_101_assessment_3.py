# Jackson Krieger
# CSCI 101 - Section A
# Python assessment 3
# References: 
# Time:

import string


with open('peter_pan.txt', 'r') as peter_pan:
    list_var = []
    list_var2 = []
    list_var3 = []
    list_var6 = []

    count = 0

    print('Would you like to print the number of times a specific word appears OR print the number of words of a specific length? (1 or 2)')
    choice = input('CHOICE> ')

    if choice == '1':
        print('Enter a word:')
        word = input('WORD> ')
        word1 = word.lower()
 
        line = peter_pan.readlines()
        
        for i in range(len(line)):
            x = line[i]
            x = x.strip()
            x = x.split()
            for word in range(len(x)):
                list_var4 = ''.join(x[word])
                list_var5 = list_var4.split(' ')
                for i in range(len(list_var5)):
                    z = list_var5[i].replace('-', ' ')
                

                    for i in string.punctuation:
                        z = z.replace(i, '')
                    z = z.lower()
                    
                    if z == word1:
                        count += 1


                        
                        
        print(f'The number of times {word1} appears in the document is:')
        print(f'OUTPUT {count}')

    if choice == '2':
        print('Enter a length:')
        length = int(input('LENGTH> '))

        count = []
        unique = []
        
        line = peter_pan.readlines()
        
        for i in range(len(line)):
            x = line[i]
            x = x.strip()
            x = x.split()
            for word in range(len(x)):
                list_var4 = ''.join(x[word])
                list_var5 = list_var4.split(' ')
                for i in range(len(list_var5)):
                    z = list_var5[i].replace('-', ' ')
                

                    for i in string.punctuation:
                        z = z.replace(i, ' ')
                    z = z.lower()
                    if len(z) == length:
                        count.append(z)

                        if z not in unique:
                            unique.append(z)
        print(f'The number of words in the document with length {length} is:')
        print(f'OUTPUT {len(count)}')
        print(f'The number of unique words in the document with length {length} is:')
        print(f'OUTPUT {len(unique)}')
