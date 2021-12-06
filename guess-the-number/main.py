from random import randint
import os

numbers = [1,2,3,4,5,6,7,8,9]
s = " "
e = "\n"


class guess():

    def __init__(self) -> None:
        pass
    
    def start(guess, range=None):
        if not '-' in range:
            return print(4*e+10*s+'You did not enter the right format'), False

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
            return print(2*e+10*s+'Congrats you picked the right number') ,True
        elif not guess == number:
            return print(2*e+10*s+f"The number was {number}, You lose"), False