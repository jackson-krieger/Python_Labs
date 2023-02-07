#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 04A
#   References: none
#   Time: 15 minutes

company_name = input('Enter company name: ')

company_location = input('Enter company city/state: ')

cashier_name = input('Enter cashier name: ')

item1_name = input('Purchased item 1 name: ')
item1_price = float(input('Purchased item 1 price: '))

item2_name = input('Purchased item 2 name: ')
item2_price = float(input('Purchased item 2 price: '))

item3_name = input('Purchased item 3 name: ')
item3_price = float(input('Purchased item 3 price: '))

total_cost = (item1_price + item2_price + item3_price)

fav_msg = input('Enter your favorite ending message: ')

print('     RECEIPT GENERATOR')
print('---------------------------')
print(f'  {company_name}')
print(f'  {company_location}')
print('===========================')
print(f'  Your cashier was: {cashier_name}')
print('   Welcmpme valued customer')
print('===========================')
print(' Item Name       Item Price')
print(f'  {item1_name}    {item1_price:.2f}')
print(f'  {item2_name}    {item2_price:.2f}')
print(f'  {item3_name}    {item3_price:.2f}')
print('===========================')
print(f'Total cost of order: {total_cost:.2f}')
print('===========================')
print(f'  {fav_msg}')
print('---------------------------')
