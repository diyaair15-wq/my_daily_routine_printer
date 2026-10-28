theboard = {'7':'','8':'','9':'','4':'','5':'','6':'','1':'','2':'','3':''}


board_keys = []
for key in theboard:
    board_keys.append(key)
    
def printboard (board):
    print(board['7']+ '|'+board['8']+ '|'+board['9']+ '|')
    print('-+-+-')
    print(board['4']+ '|'+board['5']+ '|'+board['6']+ '|')
    print('-+-+-')
    print(board['1']+ '|'+board['2']+ '|'+board['3']+ '|')
    
def game():
    
    turn = 'x'
    count = 0
    
    
    for i in range(10):
        printboard(theboard)
        print("it's your turn ,"+ turn +".move to which place")
        move = input()
        
        if theboard[move] == '':
            theboard[move] = turn
            count += 1
        else:
            print("that place is already filled . move to new place")
            continue
        
        if count  >= 5:
            if theboard['7']==theboard['8']==theboard['9'] != '': 
                
                printboard
               
        
        