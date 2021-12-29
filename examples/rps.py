import games

c = input("Choose rock, paper or scissor > ")

output = games.rps(c)

if output[2] is False:
    print(f'Loser, You picked {output[0]}, AI picked {output[1]}')
elif output[2] is True:
    print(f'Winner, You picked {output[0]}, AI picked {output[1]}')
elif output[2] == None:
    print(f"{output[1]}, {output[0]}")