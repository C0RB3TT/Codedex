# Checkpoint Project for Codedex Python
import random

while True:
  computer = random.randint(1, 3)
  print('''
  ROCK PAPER SCISSORS''')
# input for the game
  player = int(input('''
      1 - Rock ✊
      2 - Paper 🫲
      3 - Scissors ✌️
      Enter a number between 1 and 3: '''))

#your choice
  if player == 1:
    print('''
      You chose Rock''')
  elif player == 2:
    print(''' 
      You chose Paper''')
  elif player == 3:
    print(''' 
      You chose Scissors''')
  else:
    print(''' 
      Wrong input''')

#computer choice
  if computer == 1:
    print('''      CPU chose Rock''')
  elif computer == 2:
    print('''      CPU chose Paper''')
  elif computer == 3:
    print('''      CPU chose Scissors''')
  else:
    print('''    CPU Malfunction''')
#starting and ending the loop in case of a tie game
  if player == computer:
    print('      Tie game, restart')
    continue
  elif player == 1 and computer == 2:
      print('      CPU wins!')
      break
  elif player == 2 and computer == 1:
      print('      You win!')
      break
  elif player == 1 and computer == 3:
      print('      You win!')
      break
  elif player == 3 and computer == 1:
      print('      CPU wins!')
      break
  elif player == 2 and computer == 3:
      print('      CPU wins!')
      break
  elif player == 3 and computer == 2:
      print('      You win!')
      break
