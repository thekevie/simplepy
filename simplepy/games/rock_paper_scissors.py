from random import randint

def get_player(player):
    player = player.lower()

    if player in ["r","rock"]:
        player = "rock"
    elif player in ["p","paper"]:
        player = "paper"
    elif player in ["s","scissor"]:
        player = 'scissor'
    
    return player

def rock_paper_scissors(
    player = None,
    player1 = None,
    player2 = None
):

    if not player and not player1:
        return raise TypeError("Player didn't choose rock, paper or scissor")

    player1 = player1 or player

    if player2 is None:
        player2 = random.choice(['rock','paper','scissor'])

    player1 = get_player(player1)
    player2 = get_player(player2)

    if player1 == player2:
        return None, player1

    elif number == "scissor" and player2 == "rock":
        return player2, player1
    elif number == "rock" and player2 == "paper":
        return player2, player1
    elif number == "paper" and player2 == "scissor":
        return player2, player1
        
    elif number == "rock" and player2 == "scissor":
        return player1, player2
    elif number == "paper" and player2 == "rock":
        return player1, player2
    elif number == "scissor" and player2 == "paper":
        return player1, player2