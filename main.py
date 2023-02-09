#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from logo import logo
print(logo)
#gera um numero de 1 a 100
secret_number = random.randint(1,100)
print(f'The secret number is:{secret_number}')
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")

def check_win(player_guess, secret):
  if player_guess > secret:
    return 'high'
  elif player_guess < secret:
    return 'low'
  elif player_guess == secret:
    return 'win'
    
#pergunta ao usuario o nivel de dificuldade
diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

if diff == "easy":
  chances = 10
else:
  chances = 5

playing_the_game = True
while playing_the_game == True:
  print(f"You have {chances} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  
  if check_win(guess, secret_number) == 'low':
    print('Your guess is too low')
    chances -= 1
    
  elif check_win(guess, secret_number) == 'high':
    print('Your guess is too high')
    chances -= 1
    
  elif check_win(guess, secret_number) == 'win':
    print(f'You got it the answer is {secret_number}')
    
  if chances == 0:
    print(f"\nYou lose the answer was {secret_number}!!")
    playing_the_game = False
