from random import randint

numbers = [1,2,3,4,5,6,7,8,9]
s = " "
e = "\n"

class guess():
    
    def start(guess, range=None):
        if not '-' in range:
            return print('You did not enter the right format'), False

        for i in str(numbers):
            if i in range:
               number = True
        
        if number is False:
            range = '1-10'

        range = str(range)

        fr, to = range.split('-')

        guess = int(guess)
        number = randint(int(fr),int(to))

        if guess == number:
            return guess, True
        elif not guess == number:
            return guess, False