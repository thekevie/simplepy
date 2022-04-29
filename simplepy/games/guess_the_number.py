from random import randint

class guess_the_number():
    
    def start(guess, range=None):

        if range is None:
            range = '1-10'

        if not '-' in range:
            return None, 'You did not enter the right format'

        range = str(range)

        fr, to = range.split('-')

        guess = int(guess)
        number = randint(int(fr),int(to))

        if guess == number:
            return True, guess
        elif not guess == number:
            return True, guess