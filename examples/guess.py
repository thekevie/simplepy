import games

g = input('Guess a number betwen 1-10 > ')

win, response = games.guess(g, '1-10')

if win is False:
    print(f'The number was {response}')
elif win is True:
    print(f'Congrats you picked the correct number, {response}')