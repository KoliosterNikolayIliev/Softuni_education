"""
Game "Tic-Tac-Toe" ver. 1.22
by S.P.™ © 09.2019
"""

from os import name, system

board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
c = 0
turn = 'X'
x = ' '
y = '|'
z = '---'


def cls():
    system('cls' if name == 'nt' else 'clear')


def drawboard():
    print('\n Positions:\n')
    print(x + y + z + y + z + y + z + y)
    for count in range(9):
        if count == 2 or count == 5 or count == 8:
            print(x + y + x + board[count] + x + y)
            print(x + y + z + y + z + y + z + y)
        else:
            print(x + y + x + board[count], end='')
    print()


cls()
print('\n Game "Tic-Tac-Toe" (for two players) ver. 1.22\n code and compilation by S.P. 01.2020')
input('\n Press <Enter> to start... ')

while True:

    try:
        cls()

        if turn == 'X':
            if board[0] == board[1] == board[2] == 'O' or board[3] == board[4] == board[5] == 'O' \
                    or board[6] == board[7] == board[8] == 'O' or board[0] == board[3] == board[6] == 'O' \
                    or board[1] == board[4] == board[7] == 'O' or board[2] == board[5] == board[8] == 'O' \
                    or board[0] == board[4] == board[8] == 'O' or board[2] == board[4] == board[6] == 'O':
                drawboard()
                print(' Player 2 WINS!!!')
                break

            cls()
            drawboard()
            pos = int(input(' Player 1, input free position number for "X"... '))

            if pos < 1 or pos > 9:
                continue
            elif board[pos - 1] == 'X' or board[pos - 1] == 'O':
                continue
            else:
                board[pos - 1] = 'X'
                turn = 'O'
        else:
            if board[0] == board[1] == board[2] == 'X' or board[3] == board[4] == board[5] == 'X' \
                    or board[6] == board[7] == board[8] == 'X' or board[0] == board[3] == board[6] == 'X' \
                    or board[1] == board[4] == board[7] == 'X' or board[2] == board[5] == board[8] == 'X' \
                    or board[0] == board[4] == board[8] == 'X' or board[2] == board[4] == board[6] == 'X':
                drawboard()
                print(' Player 1 WINS!!!')
                break

            cls()
            drawboard()
            pos = int(input(' Player 2, input free position number for "O"... '))

            if pos < 1 or pos > 9:
                continue

            if board[pos - 1] == 'X' or board[pos - 1] == 'O':
                continue
            else:
                board[pos - 1] = 'O'
                turn = 'X'
        c += 1
    except ValueError:
        continue

    if c >= 9:
        cls()
        drawboard()
        print(' DRAW!!!')
        break

input('\n Press <Enter> to exit...')
cls()