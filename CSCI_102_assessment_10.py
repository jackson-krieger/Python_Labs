#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 10
#   References: Got help from TA Drew
#   Time: 30 minutes

import csv

list1 = []

with open('formations.csv', 'r') as rocks:
    var1 = csv.reader(rocks)
    with open('formations_parsed.csv', 'w') as rocks_list:
        var2 = csv.writer(rocks_list)
        header = ['Depth', 'Start Depth', 'End Depth', 'Difference in Depth', 'Formation', 'Age of Formation']
        var2.writerow(header)
        next(var1)
        for i in var1:
            depth = i[0]
            split = depth.split('-')
            start = float(split[0])
            end = float(split[1])
            difference = round(end - start, 2)
            formation = i[1]
            list1.append(depth)
            list1.append(start)
            list1.append(end)
            list1.append(f'{difference:.2f}')
            list1.append(formation)
            if start < 700:
                list1.append('Paleocene')
            else:
                list1.append('Cretaceous')
            var2.writerow(list1)
            list1 = []
