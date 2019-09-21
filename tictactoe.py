theboard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'bot-l':' ','bot-m':' ','bot-r':' ',}
def printtheboard(board):
    print(board['top-l']+'|'+board['top-m']+'|'+board['top-r'])
    print('-+-+-')
    print(board['mid-l']+'|'+board['mid-m']+'|'+board['mid-r'])
    print('-+-+-')
    print(board['bot-l']+'|'+board['bot-m']+'|'+board['bot-r'])
#printtheboard(theboard)
turn='X'
for i in range(9):
    printtheboard(theboard)
    print('Turn for'+turn+'. Move on which space?')
    move=input()
    theboard[move]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
printtheboard(theboard)
