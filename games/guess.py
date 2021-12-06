from random import randint

class guess():
    
    def start(guess, range=None):

        if range is None:
            range = '1-10'

        if not '-' in range:
            return print('You did not enter the right format'), None

        range = str(range)

        fr, to = range.split('-')

        guess = int(guess)
        number = randint(int(fr),int(to))

        if guess == number:
            return guess, True
        elif not guess == number:
            return guess, False