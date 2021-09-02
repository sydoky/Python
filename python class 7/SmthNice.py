''' #(rock paper scissors) I ask name of the player 1 and 2, at least 3 characters, use while loop
class RockPaperScissors:
    def __init__(self):  # like a big boss

class Weapon:
    def __init__(self):
        self.weapon = []
'''

weapons = ["paper", "rock", "scissors"]
players = []
player1 = None
player2 = None
while player1 is None:
    player1 = input("Player1, enter your name: ")
    if not player1.isalpha():
        print("Please enter valid name that contains only letters")
        player1 = None  # this line reset the name and ask again
    if len(player1) < 3:
        print("This name should be longer than 3 letters")
        player1 = None
players.append(player1)
while player2 is None:
    player2 = input("Player2, enter your name: ")
    if not player2.isalpha():
        print("Please enter valid name that contains only letters")
        player2 = None  # this line reset the name and ask again
    if len(player2) < 3:
        print("This name should be longer than 3 letters")
        player2 = None
    if player1 == player2:
        print("This name is already taken")
        player2 = None
players.append(player2)
print(players)
player1_wins = 0
player2_wins = 0

while True:

    weapon1 = None
    weapon2 = None

    while weapon1 is None:
        weapon1 = input(player1 + " please choose your weapon from the list: rock, paper, scissors: ")
        if weapon1 not in weapons:
            print("This is not a valid choice")
            weapon1 = None
    while weapon2 is None:
        weapon2 = input(player2 + " please choose your weapon from the list: rock, paper, scissors: ")
        if weapon2 not in weapons:
            print("This is not a valid choice")
            weapon2 = None
    if weapon1 == weapon2:
        print("it's a draw")
    elif weapon1 == "rock" and weapon2 == "paper":
        print(player2 + " wins this round")
        player2_wins += 1
    elif weapon1 == "paper" and weapon2 == "scissors":
        print(player2 + " wins this round")
        player2_wins += 1
    elif weapon1 == "scissors" and weapon2 == "rock":
        print(player2 + " wins this round")
        player2_wins += 1
    elif weapon1 == "rock" and weapon2 == "scissors":
        print(player1 + " wins this round")
        player1_wins += 1
    elif weapon1 == "scissors" and weapon2 == "paper":
        print(player1 + " wins this round")
        player1_wins += 1
    elif weapon1 == "paper" and weapon2 == "rock":
        print(player1 + " wins this round")
        player1_wins += 1
    print("current score: ", player1, player1_wins, ": ", player2, player2_wins)
    if player1_wins == 3:
        print("The champion is ", player1)
        break
    if player2_wins == 3:
        print("The champion is ", player2)
        break



    player1_answer = None
    player2_answer = None
    while player1_answer is None:
        player1_answer = input(player1 + "Would you like to play again?")
        if player1_answer.lower() not in ["yes", "y"]:
            break
    if player1_answer not in ["yes", "y"]:  # we are doing this for the main loop
        break
    while player2_answer is None:
        player2_answer = input(player2 + "Would you like to play again?")
        if player2_answer.lower() not in ["yes", "y"]:
            break
    if player2_answer not in ["yes", "y"]:
        break

print("The End, chickens")











# for hw 1 king and 5 queens
















#for hw do the same for player 2 and try to see who won and print the winner












