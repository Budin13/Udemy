rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

list = [rock, paper, scissors]
game = 1
while 1:
    eugene = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.")
    )

    if eugene > 2:
        print("number not in the choices")
        continue

    print("Me: " + list[eugene])

    comp = random.randint(0, 2)
    print("Computer:" + list[comp])

    if comp == eugene:
        print("Draw")
    elif eugene == 0 and comp == 2:
        print("You Win")
    elif eugene == 2 and comp == 0:
        print("You Lose")
    elif eugene == 2 and comp == 1:
        print("You Win")
    elif eugene == 1 and comp == 2:
        print("You Lose")
    elif eugene == 1 and comp == 0:
        print("You Win")
    elif eugene == 0 and comp == 1:
        print("You Lose")

    game = input(" Type 1 if you want to play Again. Type 0 if you want to quit.")
    if game == "1":
        continue
    else:
        break
