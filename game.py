"""A number-guessing game."""

import random
import math

player_name = raw_input('Howdy, what\'s your name?\n(type in your name) ')
scores = []


def main_game():
    max_num = add_range()
    turn_limit = limit_tries()
    secret_number = random.randint(1, max_num)
    print "I'm thinking of a number between 1 and {}. \
    \nTry to guess my number.".format(max_num)

    guess_count = 0

    while True:
        if turn_limit is not None:
            turns_left = turn_limit - guess_count
            print 'You have %d tries left.' % turns_left
        player_guess = raw_input('Your guess? ')
        try:
            player_guess = int(float(player_guess))
            guess_count += 1
        except ValueError:
            print 'That\'s not a number!'
            continue
        if player_guess < 1 or player_guess > max_num:
            print 'That isn\'t a number between 1 and {}!'.format(max_num)
            continue
        if player_guess != secret_number:
            if turn_limit is not None:
                if guess_count == turn_limit:
                    print 'Too many tries! The number was %d.' % (secret_number)
                    break
            if player_guess < secret_number:
                print 'Your guess is too low, try again.'
            elif player_guess > secret_number:
                print 'Your guess is too high, try again.'
        else:
            score = int(100 * math.log(max_num, 2) / guess_count)
            scores.append(score)
            print 'Well done, %s! You found my number in %d tries.' % \
                (player_name, guess_count)
            print 'Your score is {}.'.format(score)
            break

    end_game()


def end_game():
    try:
        print 'Your best score is {}.'.format(max(scores))
    except ValueError:
        pass
    play_again = raw_input("Press Y to play again: ")
    if play_again.upper() == "Y":
        main_game()
    else:
        exit()


def limit_tries():
    limit_prompt = raw_input('Press Y for a limit on your guesses: ')
    if limit_prompt.upper() == 'Y':
        while True:
            max_tries = raw_input('Enter a max number of tries: ')
            try:
                max_tries = int(float(max_tries))
                return max_tries
            except ValueError:
                print 'That\'s not a number!'
                continue
    else:
        return None


def add_range():
    user_range = raw_input("Enter a range number (default 100): ")
    try:
        user_range = int(float(user_range))
    except ValueError:
        user_range = 100
    return user_range


main_game()
