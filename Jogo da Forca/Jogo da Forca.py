number_lifes = 5
correct_word = ['B', 'a', 'n', 'a', 'n', 'a']
correct_letters = []

while True:
    acertou = False
    letter = input ('Enter a letter: ')
    
    if number_lifes > 0:
        for i in correct_word:
            if letter == i:
                acertou = True
                correct_letters.append(letter)
        
        string = ""
        for l in correct_word:
            if l in correct_letters:
                string+= l + " "
            else:
                string+= "_ "   

        print(string)

        if not acertou:
            number_lifes-=1
            print("Erraste! Só te restam " + str(number_lifes) + " vidas")
    elif number_lifes == 0:
        break
        

