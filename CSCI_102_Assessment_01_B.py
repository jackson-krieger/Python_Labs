#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 01A
#   References: Drew helped with figuring out why code was incorrect
#   Time: 20 minutes

print('Input the total length of fencing available (in yards).')
Length = int(input('LENGTH> '))

Length_feet = (Length * 3)

Fence_sides = (Length_feet / 4)

print('The maximum rectangular area that can be bound (in feet) is:')
print('OUTPUT', round((Fence_sides ** 2), 1))


