import random

user_action = input('Enter a choice (rock, paper, scissor):')

possible_actions = ['rock', 'paper', 'scissors']

computer_actions = random.choice(possible_actions)

print(f"\nYou chose {user_action}, computer chose {computer_actions}.\n")

if user_action == computer_actions:
    print(f'Both players selected {user_action}. It''s tied!')

elif user_action == 'rock':
    if computer_actions == 'scissors':
        print('You win!')
    else:
        print('You lose!')

elif user_action == 'paper':
    if computer_actions == 'rock':
        print('You win!')
    else:
        print('You lose!')

elif user_action == 'scissors':
    if computer_actions == 'paper':
        print('You win!')
    else:
        print('You lose!')

#Output is displayed in Terminal.

    