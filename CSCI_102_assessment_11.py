#   Jackson Krieger
#  ​ CSCI 102 – Section A
#   Assessment 11
#   References: Went to office hours
#   Time: 1 hour

# import math directory
import math

# string
def print_output(string):
    print(f'OUTPUt {string}')

# cylinder volume
def cylinder_vol(radius, height):
    area = 3.1415 * radius ** 2
    volume = area * height
    volume = round(volume, 2)
    print_output(f'{volume:.2f}')

# pounds to kilograms
def lbs_to_kg(pounds):
    kg = pounds * 0.4536
    kg = round(kg, 4)
    print_output(f'{kg:.4f}')

# rectangular to polar
def polar_coords(x,y):
    r = math.sqrt(x ** 2 + y ** 2)
    r = round(r, 2)
    theta = (math.atan(y/x)) * 180 / math.pi
    theta = round(theta, 2)
    print_output(f'r: {r:.2f}')
    print_output(f'theta: {theta:.2f}')

# yen to dollars
def yen_to_dollars(yen):
    dollars = yen / (1 / 0.0068)
    dollars = round(dollars, 2)
    print_output(f'{dollars:.2f}')

# quadratic formula
def quad_form(a, b, c):
    out_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    out_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if out_1 >= out_2:
        large = out_1
        small = out_2
    else:
        large = out_2
        small = out_1
    small = int(round(small, 0))
    large = int(round(small, 0))
    print_output(small)
    print_output(large)
