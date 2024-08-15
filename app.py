import random
import time

while True:
    numbers = random.randrange(1, 500)
    while True:
        user_input = input('Guess the number: ')
        if not user_input.isdigit ():
            print('You must enter a number!')
        else:
            user_input = int(user_input)
            if user_input == numbers:
                print('Congratulations! You guessed the correct number.')
                time.sleep(1.5)
                break
            else:
                try_again = input(f'The number was: {numbers}. You entered: {user_input}. Try again? y/n ')
                if try_again.lower() in ['yes', 'y']:
                    break
                else:
                    print('See you next time!')
                    time.sleep(1.5)
                    exit()
