import random, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

guess = raw_input('Guess the coin toss! Enter heads or tails:')
def f(guess):
    while guess not in ('heads', 'tails'):
        print 'Please enter heads or tails:'
        guess = raw_input()
    if guess == 'heads':
        guess = 1
    else:
        guess = 0
    return guess
guess = f(guess)
logging.debug('guess is %s' % (guess))
toss = random.randint(0, 1)
logging.debug('toss is %s' % (toss))
if toss == guess:
    print 'You got it!'
else:
    guess = raw_input('Nope! Guess again!')
    guess = f(guess)
    logging.debug('guess is %s' % (guess))
    logging.debug('toss is %s' % (toss))
    if toss == guess:
        print 'You got it!'
    else:
        print 'Nope! You are really bad at this game.'
