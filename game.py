"""A number-guessing game."""

import random

player_name = raw_input('Howdy, what\'s your name?\n(type in your name) ')
secret_number = random.randint(1, 100)
print "I'm thinking of a number between 1 and 100.\nTry to guess my number."

guess_count = 1

while True:
    player_guess = int(raw_input('Your guess? '))
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
