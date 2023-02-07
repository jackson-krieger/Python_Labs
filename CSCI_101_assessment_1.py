# Jackson Krieger
# CSCI 101 - Section A
# Python assessment 1
# References: TA Zach helped figure out why 3 tests were failing
# Time: 1 hour

print('How many minutes early would you like your alarm to go off?')
minutes_early = int(input('EARLY> '))

print('What time do you need to get out of bed?')
out_bed_hours = int(input('HOURS> '))
out_bed_minutes = int(input('MINUTES> '))

time_minutes = (((out_bed_hours * 60) + out_bed_minutes) - minutes_early)
alarm_hour = time_minutes / 60
alarm_minutes = time_minutes % 60

if time_minutes < 0:
    alarm_hour = 24 + (time_minutes / 60)
else:
    alarm_hour = time_minutes / 60

print('You should set your alarm for:')
print(f'OUTPUT {int(alarm_hour):0>2} {alarm_minutes:0>2}')   
