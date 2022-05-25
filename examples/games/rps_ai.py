import games

c = input("Choose rock, paper or scissor > ")

win, you, ai = games.rps.ai(c)

if win is False:
    print(f'Loser, You picked {you}, AI picked {ai}')
elif win is True:
    print(f'Winner, You picked {you}, AI picked {ai}')
elif win is None:
    print(f"Draw, You picked {you}, AI picked {ai}")