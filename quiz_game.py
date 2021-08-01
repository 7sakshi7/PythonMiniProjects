print('******************************** Welcome To Quiz Game ********************************')

want_to_play = input('Do you want to play? y/n ')

if want_to_play == 'n':
    quit()
print('\n')
print('Lets play :)')

score = 0

print('\n')
print('Question 1 ----------->')
answer = input('What is latest version of python? ')
if answer == '3.7.9':
    score+=1
    print('correct answer')
else:
    print('Incorrect answer')


print('\n')
print('Question 2 ----------->')
answer = input('What is latest version of python? ')
if answer == '3.7.9':
    score+=1
    print('correct answer')
else:
    print('Incorrect answer')


print('\n')
print('Question 3 ----------->')
answer = input('What is latest version of python? ')
if answer == '3.7.9':
    score+=1
    print('correct answer')
else:
    print('Incorrect answer')


print('\n')
print('Question 4 ----------->')
answer = input('What is latest version of python? ')
if answer == '3.7.9':
    score+=1
    print('correct answer')
else:
    print('Incorrect answer')


print('\n')
print('Question 5 ----------->')
answer = input('What is latest version of python? ')
if answer == '3.7.9':
    score+=1
    print('correct answer')
else:
    print('Incorrect answer')


print('\n')
print('Question 6 ----------->')
answer = input('What is latest version of python? ')
if answer == '3.7.9':
    score+=1
    print('correct answer')
else:
    print('Incorrect answer')


print('\n')
print('*******************Congratulations on completing this game*******************')
print(f'You have scored {score} marks')

