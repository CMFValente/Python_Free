hours =  int (input ('Enter a number from 0 to 23: '))
minutes = int(input ('Enter a number from 0 to 59: '))

str_clock = ''

if hours < 10:
    str_clock += '0'
str_clock += str(hours) + ':'

if minutes < 10:
    str_clock += '0'
str_clock += str(minutes)

print (str_clock)
