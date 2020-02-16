import random

wins = 0
losses = 0
ties = 0

print('ROCK,PAPER,SCISSORS')
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    ch = input()
    rd = random.choice('psr')
    # user choices
    if ch == 'p':
        print('PAPER versus')
    elif ch == 's':
        print('SCISSORS versus')
    elif ch == 'r':
        print('ROCK versus')
    # computer choices
    if rd == 'p':
        print('PAPER')
    elif rd == 's':
        print('SCISSORS')
    elif rd == 'r':
        print('ROCK')

    if ch == rd:
        print('It is a tie!')
        ties += 1
    else:
        if ch == 'p' and rd == 'r':
            print('You win!')
            wins += 1
        if ch == 'p' and rd == 's':
            print('You lose!')
            losses += 1

        if ch == 'r' and rd == 's':
            print('You win!')
            wins += 1
        if ch == 'r' and rd == 'p':
            print('You lose!')
            losses += 1

        if ch == 's' and rd == 'p':
            print('You win!')
            wins += 1
        if ch == 's' and rd == 'r':
            print('You lose!')
            losses += 1
    if ch == 'q':
        break
