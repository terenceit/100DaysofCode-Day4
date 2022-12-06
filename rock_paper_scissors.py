import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rps = [rock, paper, scissors]

#Get user input for R, P or S
player1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Print R, P, or S based on user input
player_symbol = rps[player1]
print(player_symbol)

#Print statement
print("Computer chose:\n")

#Print R, P, or S at random
computer = random.randint(0, 2)
comp_symbol = rps[computer]
print(comp_symbol)

#Decide on winner
#Player 1 - Rock & Computer - Paper = Lose
if player_symbol == rps[0] and comp_symbol == rps[1]:
    print("You lose!")
#Player1 - Rock & Computer - Scissors = Win
elif player_symbol == rps[0] and comp_symbol == rps[2]:
    print("You win!")
#Player1 - Paper & Computer - Rock = Win
elif player_symbol == rps[1] and comp_symbol == rps[0]:
    print("You win!")
#Player1 - Paper & Computer - Scissors = Lose
elif player_symbol == rps[1] and comp_symbol == rps[2]:
    print("You lose!")
#Player1 - Scissors & Computer - Rock = Lose
elif player_symbol == rps[2] and comp_symbol == rps[0]:
    print("You lose!")
#Player1 - Scissors & Computer - Paper = Win
elif player_symbol == rps[2] and comp_symbol == rps[1]:
    print("You win!")
#Draw
else:
    print("Draw!")
