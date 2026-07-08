import random

while True:
    try:
        number = int(input('Level: '))
    except ValueError:
        continue
    if number < 1:
        continue
    else:
        randnumber = random.randint(1, number)
        break

while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        continue
    if guess < 1:
        continue
    if guess < randnumber:
        print('Too small!')
    elif guess > randnumber:
        print('Too large!')
    else:
        print('Just right!')
        break