from random import randint

class rock_paper_scissors():

    def ai(choice):

        if choice is None:
            return("You didn't choose rock, paper or scissor")

        choice = choice.lower()

        if choice == 'r':
            choice = 'rock'
            number = 1
        elif choice == 'p':
            choice = 'paper'
            number = 2
        elif choice == 's':
            choice = 'scissor'
            number = 3

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
            return None, choice, picked

        elif number == 3 and ai == 1:
            return False, choice, picked
        elif number == 1 and ai == 2:
            return False, choice, picked
        elif number == 2 and ai == 3:
            return False, choice, picked
        
        elif number == 1 and ai == 3:
            return True, choice, picked
        elif number == 2 and ai == 1:
            return True, choice, picked
        elif number == 3 and ai == 2:
            return True, choice, picked
        
        
    def user(choice1, choice2):

        if choice1 is None:
            return("You didn't choose rock, paper or scissor")

        choice1 = choice1.lower()
        choice2 = choice2.lower()

        if choice1 == 'r':
            choice1 = 'rock'
            number1 = 1
        elif choice1 == 'p':
            choice1 = 'paper'
            number1 = 2
        elif choice1 == 's':
            choice1 = 'scissor'
            number1 = 3

        if choice1 == 'rock':
            number1 = 1
        elif choice1 == 'paper':
            number1 = 2
        elif choice1 == 'scissor':
            number1 = 3
            
            
        if choice2 == 'r':
            choice2 = 'rock'
            number2 = 1
        elif choice2 == 'p':
            choice2 = 'paper'
            number2 = 2
        elif choice2 == 's':
            choice2 = 'scissor'
            number2 = 3

        if choice2 == 'rock':
            number2 = 1
        elif choice2 == 'paper':
            number2 = 2
        elif choice2 == 'scissor':
            number2 = 3


        if number1 == number2:
            return None, choice1, choice2

        elif number1 == 3 and number2 == 1:
            return choice1, choice2
        elif number1 == 1 and number2 == 2:
            return choice1, choice2
        elif number1 == 2 and number2 == 3:
            return choice1, choice2
        
        elif number1 == 1 and number2 == 3:
            return choice1, choice2
        elif number1 == 2 and number2 == 1:
            return choice1, choice2
        elif number1 == 3 and number2 == 2:
            return choice1, choice2