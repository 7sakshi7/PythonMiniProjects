import random
import words_for_game as wrd
import re

# regular expression
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:0-9]')

# choosing one random word from list of words
random_word = random.choice(wrd.words)
# print(random_word)

# total lives will be equal to length of the word
lives = len(random_word)
word = random_word

already_guessed = []

# letters which user will guess we will add to this other wise it will fill with -
user_guess= '-'*lives
# print(user_guess)

# it will run untill the word becones equal to the random word
while user_guess !=random_word:
    # decrement lives every single time
    lives-=1

    # if lives is less than zero means no chance
    if lives <0:
        print('-----------------------SORRY , LIVES ARE OVER -------------------- \n')
        break
    
    print(f'Lives remaining is {lives+1} English Word is {user_guess}')
    print(f'Already Guessed characters ----> ',end=' ')
    print(already_guessed)
    char = input('Guess a letter (Lower and Upper case letters will be treated as same): ')
    # checking wether user has enter more than one character
    if len(char)>1:
        print('Enter only a character ')
        continue

    if ord(char) >= ord('A') and ord(char)<= ord('Z'):
        no = chr(ord(char)+32)
        char = no

    #checking for special characters
    if regex.search(char)!=None:
        print('Enter only a character ')
        continue

    # if words is not already gussesed and its there in random words
    elif char in word:
        index = word.find(char)
        user_guess = user_guess[0:index] + char + user_guess[index+1:]
        word = word[0:index] + '#' + word[index+1:]
        print(char,type(char))

    # user already guessed it
    elif char in user_guess:
        print('Already Guessed-------This character will no reapeat again')

    # wrong choice
    else:
        print('Oops Worng Choice :(')

    print('\n')
    if char in already_guessed:
        continue
    else:
        already_guessed.append(char)

if user_guess == random_word:
    print('\n -----------------------WELL DONE---------------, YOU DID IT---------------------')
        


