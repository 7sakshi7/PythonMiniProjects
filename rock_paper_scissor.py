import random
import re
print('******************************** Welcome To Quiz Game ********************************')

user_wins = 0
computer_wins = 0

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:A-Za-z]')

print('**********Rules**********')
print('1 for Rock \n 2 for Paper \n 3 for Scissor')
print('Enter any number from 1 to 3 and computer will also choose one and then decide winner')

while True:
    want_to_play = input('Do you want to play? y/n ')
    if want_to_play == 'n':
        break
    print('\n')
    print('Lets play :)')

    answer = input('Enter any number from 1-3')
    if regex.search(answer)!=None:
        print('Enter only numbers')
        break 
    answer = int(answer)
    
    if answer <1 or answer>3:
        print('Enter only numbers')
        break 
    
    computer_answer = random.randint(1,3)

    # User chooses 1

    if answer == 1 and computer_answer == 1:
        print('Both chooses Rock')
        print('.......DRAW..........')
    
    elif answer == 1 and computer_answer == 2:
        print('You choode Paper and computer chooses Rock')
        print('Computer Won')
        computer_wins+=1
    
    elif answer == 1 and computer_answer == 3:
        print('You choode Rock and computer chooses Scissor')
        print('You Won')
        user_wins+=1
    
    # User chooses 2
    
    elif answer == 2 and computer_answer == 1:
        print('You choose Paper and computer chooses Rock')
        print('Computer Won')
        computer_wins+=1
    
    elif answer == 2 and computer_answer == 2:
        print('You Both chooses Paper')
        print('.......DRAW..........')
    
    elif answer == 2 and computer_answer == 3:
        print('You choose Paper and computer chooses Scissor')
        print('Computer Won')
        computer_wins+=1

    # User chooses 3
    
    elif answer == 3 and computer_answer == 1:
        print('You choose Scissor and computer chooses Rock')
        print('Computer Won')
        computer_wins+=1
    
    elif answer == 3 and computer_answer == 2:
        print('You choose Scissor and computer chooses paper')
        print('You Won')
        user_wins+=1
    
    elif answer == 3 and computer_answer == 3:
        print('You both chooses Scissor')
        print('.......DRAW..........')


print(f'Your Wins ---> {user_wins} and computer wins ---> {computer_wins}')