import time

print('Hello User, guess a number between 1 and 1000, \'X\' will end the game.')
while True:
    print('Number: ', end = '')
    guess = input()
    if guess in ('X', 'x'):
        print('Quitting the game ...')
        time.sleep(1)
        break
    try:
        valid_guess = int(guess)
        if valid_guess < 10000:
            if valid_guess % 2 == 0:
                print(f'{valid_guess} is an even number! Have another?')
            elif valid_guess % 2 != 0:
                print(f'{valid_guess} is an odd number! Have another?')
        else:
            print(f'{valid_guess} is over 1000, try again with a small number!')
    except ValueError:
        print("That's not a number, try again!")
