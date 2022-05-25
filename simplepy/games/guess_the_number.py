from random import randint
from ..convert import convert
    
def guess_the_number(guess, range = None):

    if range is None:
        range = '1-100'

    if not '-' in range:
        return raise TypeError("{0} is a invalid format".format(range))

    fr, to = range.split('-')

    guess = convert(guess, to=int)
    number = randint(int(fr),int(to))

    if guess == number:
        return True, guess
    elif not guess == number:
        return False, number