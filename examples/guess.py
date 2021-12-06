import games

g = input('Guess a number betwen 1-10 > ')

output = games.guess(g, '1-10')

if output[1] is False:
    print(f'The number was {output[0]}')
elif output[1] is True:
    print(f'Congrats you picked the correct number, {output[0]}')