"""A number-guessing game."""

import random

player_name = raw_input('Howdy, what\'s your name?\n(type in your name) ')
secret_number = random.randint(1, 100)
print "I'm thinking of a number between 1 and 100.\nTry to guess my number."

guess_count = 1

while True:
    player_guess = raw_input('Your guess? ')
    try:
        player_guess = int(float(player_guess))
    except ValueError:
        print 'That\'s not a number!'
        continue
    if player_guess < 1 or player_guess > 100:
        print 'That isn\'t a number between 1 and 100!'
        continue
    if player_guess != secret_number:
        guess_count += 1
        if player_guess < secret_number:
            print 'Your guess is too low, try again.'
        elif player_guess > secret_number:
            print 'Your guess is too high, try again.'
    else:
        print 'Well done, %s! You found my number in %d tries.' % \
            (player_name, guess_count)
        break
