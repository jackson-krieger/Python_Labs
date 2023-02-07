#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 04B
#   References: Worked out kinks with neighbor
#   Time: 1 hour

# inputs
print('Input the chemical elements of the amino acid:')
carbon = int(input('CARBON> '))
hydrogen = int(input('HYDROGEN> '))
nitrogen = int(input('NITROGEN> '))
oxygen = int(input('OXYGEN> '))
sulfur = int(input('SULFUR> '))

# use carbon value to identify glutamine
if carbon == 5:
    print('The amino acid for 5C--10H--2N--3O--0S is Glutamine')
    print('OUTPUT 5C--10H--2N--3O--0S')
    print('OUTPUT Glutamine')

# use hydrogen to identify arginine 
elif hydrogen == 14:
    print('The amino acid for 6C--14H--4N--2O--0S is Arginine')
    print('OUTPUT 6C--14H--4N--2O--0S')
    print('OUTPUT Arginine')

# use hydrogen to identify histidine
elif hydrogen == 9:
    print('The amino acid for 6C--9H--3N--2O--0S is Histidine')
    print('OUTPUT 6C--9H--3N--2O--0S')
    print('OUTPUT Histidine')

# use sulfur to identify cysteine
elif sulfur == 1:
    print('The amino acid for 3C--7H--1N--2O--1S is Cysteine')
    print('OUTPUT 3C--7H--1N--2O--1S')
    print('OUTPUT Cysteine')

# use carbon to identify asparagine 
elif carbon == 4:
    print('The amino acid for 4C--8H--2N--3O--0S is Asparagine')
    print('OUTPUT 4C--8H--2N--3O--0S')
    print('OUTPUT Asparagine')

# use carbon and sulfur to identify alanine
elif carbon == 3 and sulfur == 0:
    print('The amino acid for 3C--7H--1N--2O--0S is Alanine')
    print('OUTPUT 3C--7H--1N--2O--0S')
    print('OUTPUT Alanine')

    
