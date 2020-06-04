import random

#choose marker to see who is X and who is O
def choose_marker():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
    
#who is first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player2'
    else:
        return 'Player1'
    
#board
def display_board(board):
    
    print('|'+board[7]+'|'+board[8]+'|'+board[9]+'|')
    print('|'+board[4]+'|'+board[5]+'|'+board[6]+'|')
    print('|'+board[1]+'|'+board[2]+'|'+board[3]+'|')
    print(chr(27) + "[2J")

#player choose position
def choose_position(marker):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(theBoard, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#cpu choose position
def cpu_position(marker):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(theBoard, position):
        position = random.randint(1,9)
        
    return position

#place marker on position
def place_marker(board,position,marker):
    board[position] = marker
    
#check if win
def check_win(board,marker):
    return ((board[7] == marker and board[8] == marker and board[9] == marker) or # across the top
    (board[4] == marker and board[5] == marker and board[6] == marker) or # across the middle
    (board[1] == marker and board[2] == marker and board[3] == marker) or # across the bottom
    (board[7] == marker and board[4] == marker and board[1] == marker) or # down the middle
    (board[8] == marker and board[5] == marker and board[2] == marker) or # down the middle
    (board[9] == marker and board[6] == marker and board[3] == marker) or # down the right side
    (board[7] == marker and board[5] == marker and board[3] == marker) or # diagonal
    (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

# check if space is available 
def space_check(board,position):
    return board[position] == ' '
#check if there is no space so tie
def check_tie(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
