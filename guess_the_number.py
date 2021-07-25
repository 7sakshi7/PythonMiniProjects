import random
import re
print('******************************** Welcome To Quiz Game ********************************')

want_to_play = input('Do you want to play? y/n ')

if want_to_play == 'n':
    quit()
print('\n')
print('Lets play :)')

random_number = random.randint(1,10)
answer=0
steps=0
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:A-Za-z]')

while True:
    steps+=1
    answer = input('Enter any number between 1 and 10')
    if regex.search(answer)!=None:
        print('Enter only numbers')
        break 
    answer = int(answer)
    if answer < 1 or answer> 10:
        print('Enter a valid number')
        break
    if answer == random_number:
        print(f'Correct answer in {steps} steps')
        break
    elif answer < random_number:
        print('Answer is too low')
        continue
    else:
        print('Answer is too high')
        continue

