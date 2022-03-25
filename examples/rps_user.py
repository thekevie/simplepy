import games

user1 = input("Choose rock, paper or scissor > ")
user2 = input("Choose rock, paper or scissor > ")

winner, loser = games.rps.user(user1, user2)

if winner == user1:
    print(f'Winner User1 picked {winner}, User2 picked {loser}')
elif winner == user2:
    print(f'Winner User2 picked {winner}, User1 picked {loser}')
elif winner is None:
    print(f"Draw, User1 picked {user1}, User2 picked {user2}")