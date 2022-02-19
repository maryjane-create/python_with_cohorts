



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn +'move in space...')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
          turn = 'X'
printBoard(theBoard)



#
# def printBoard(board):
#     print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
#     print('-+-+-')
#     print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
#     print('-+-+-')
#     print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
#     turn ='X'
#
#     # for i in range(9):
#     #     printBoard(theBoard)
#     #     print('turn for'+turn+'move on space')
#     #     move=input()
#     #     theBoard[move]=turn
#     #     if turn=='X':
#     #         turn='O'
#     #     else:
#     #         turn='X'
#     # printBoard(theBoard)
#
#
# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M':
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
# printBoard(theBoard)