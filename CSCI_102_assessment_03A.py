# Jackson Krieger
# CSCI 102 - Section A
# Python lab 03A
# References: zyBooks reference code
# Time: 10 minutess

print('Enter the Tweet or Message abbreviation to decode')

tweet = input('TWEET> ')

print('The decoded abbreviation is:')

if tweet == 'LOL':
    print('OUTPUT LOL = Laughing out loud')

elif tweet == 'BFN':
    print('OUTPUT BFN = Bye for now')

elif tweet == 'FTW':
    print('OUTPUT FTW = For the win')

elif tweet == 'IRL':
    print('OUTPUT IRL = In real life')

elif tweet == 'BTW':
    print('OUTPUT BTW = By the way')

elif tweet == 'DM':
    print('OUTPUT DM = Direct message')

elif tweet == 'AFAIK':
    print('OUTPUT AFAIK = As far as I know')

elif tweet == 'IDK':
    print("OUTPUT IDK = I don't know")

else:
    print("Sorry, don't know that one")
