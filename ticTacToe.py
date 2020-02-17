theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
    ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'
printBoard(theBoard)
for i in range(8):
    print('It is ' + turn + '  Make your movement!')
    move = input()
    theBoard[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

    printBoard(theBoard)
