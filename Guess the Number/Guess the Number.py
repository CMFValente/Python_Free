import random
correct_answer = random.randint(0,100)

while True:
    number = int (input ('Enter a number:'))
    if correct_answer == number:
        print ('Correct!')
        break
    if correct_answer < number:
        print ('Wrong! It\'s smaller than ' + str(number))
    elif correct_answer > number :
        print ('Wrong! It\'s greater than ' + str(number))