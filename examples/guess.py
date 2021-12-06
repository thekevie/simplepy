import games

g = input('Guess a number betwen 1-10 > ')

answer = games.guess.start(g, '1-10')

if answer[1] is False:
    print(f'The number was {answer[0]}')
elif answer[1] is True:
    print(f'Congrats you picked the correct number, {answer[0]}')