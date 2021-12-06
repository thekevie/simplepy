from random import randint

class rps():

    def start(choice):

        if choice is None:
            return("You didn't choose rock, paper or scissor")

        choice = choice.lower()

        if choice == 'rock':
            number = 1
        elif choice == 'paper':
            number = 2
        elif choice == 'scissor':
            number = 3

        ai = randint(1,3)

        if ai == 1:
            picked = 'rock'
        elif ai == 2:
            picked = 'paper'
        elif ai == 3:
            picked = 'scissor'

        if number == ai:
            return print(f"You both choose {choice}"), None

        elif number == 3 and ai == 1:
            return choice, picked, False
        elif number == 1 and ai == 2:
            return choice, picked, False
        elif number == 2 and ai == 3:
            return choice, picked, False
        
        elif number == 1 and ai == 3:
            return choice, picked, True
        elif number == 2 and ai == 1:
            return choice, picked, True
        elif number == 3 and ai == 2:
            return choice, picked, True