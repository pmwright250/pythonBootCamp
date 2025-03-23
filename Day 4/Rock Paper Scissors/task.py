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

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
valid = 0
while valid == 0:
    if choice == 0:
        valid = 1
        print(rock)
    elif choice == 1:
        valid = 1
        print(paper)
    elif choice == 2:
        valid = 1
        print(scissors)
    else:
        print("That is not a valid option. Please try again.")

computer_choice = random.randint(0,2)
choice_list = [rock,paper,scissors]
print("Computer chose:")
print(choice_list[computer_choice])

if choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and choice == 2:
    print("You lose!")
elif computer_choice > choice:
    print("You lose!")
elif choice > computer_choice:
    print("You win!")
elif computer_choice == choice:
    print("It's a draw!")