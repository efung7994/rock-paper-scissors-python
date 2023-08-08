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
def game():
  play = input("Let's play! 0 for rock, 1 for paper, 2 for scissors \n")
  choices = [rock, paper, scissors]
  player_choice = choices[int(play)]
  computer_choice = random.choice(choices)

  print(player_choice)
  print(computer_choice)

  if player_choice == computer_choice:
      print("It's a Tie!")

  if player_choice == rock:
      if computer_choice == paper:
          print("You Lose!")
      elif computer_choice == scissors:
          print("You Win!")

  if player_choice == paper:
      if computer_choice == scissors:
          print("You Lose!")
      elif computer_choice == rock:
          print("You Win!")

  if player_choice == scissors:
      if computer_choice == rock:
          print("You Lose!")
      elif computer_choice == paper:
          print("You Win!")
  game()

game()