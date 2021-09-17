hours =  23
minutes = 59

def printTime(hours, minutes):
    str_clock = ''

    if hours < 10:
        str_clock += '0'
    str_clock += str(hours) + ':'

    if minutes < 10:
        str_clock += '0'
    str_clock += str(minutes)

    print (str_clock)

while True:
    command = input('Escreva o comando > ')
    if command == "exit":
        print ('Adeus') 
        break
    if command == 'tick m':
        minutes+=1
        if minutes > 59:
            minutes = 0
    elif command == 'tick h':
        hours+=1
        if hours > 23:
            hours = 0
    
    printTime(hours, minutes)


