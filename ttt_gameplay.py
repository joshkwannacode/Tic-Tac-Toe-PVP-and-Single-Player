"""
Simple tic tac toe game that has an option to play pvp or single player

"""
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

print('Welcome to tic tac toe')
choose = input('Choose pvp or single player').lower() #choose pvp or single player

player1,player2 = choose_marker() #determines who has x or o

theBoard = [' '] * 10 #create playing board

turn = choose_first()
print(turn + ' will go first.')
   
game_on = True # used to end the game

if choose == 'pvp':
    while game_on:
        if turn == 'Player1':
            
            #shows the board then player choose position
            display_board(theBoard)
            position = choose_position(theBoard)
            place_marker(theBoard,position,player1)
            
            if check_win(theBoard, player1):
                display_board(theBoard) 
                print('Player1 has won')
                game_on = False
                a = 0
            else:
                if check_tie(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    a = 0
                    break
                else:
                    turn = 'Player2'

        else:
            # Player2's turn.
            display_board(theBoard)
            position = choose_position(theBoard)
            place_marker(theBoard,position,player2)
            
            if check_win(theBoard, player2):
                display_board(theBoard) 
                print('Player1 has won')
                a = 0
                game_on = False
            else:
                if check_tie(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    a = 0
                    break
                else:
                    turn = 'Player1'
                    

                
else:
    while game_on:
        if turn == 'Player1':
            
            #shows the board then player choose position
            display_board(theBoard)
            position = choose_position(theBoard)
            place_marker(theBoard,position,player1)
            
            if check_win(theBoard, player1):
                display_board(theBoard) 
                print('Player1 has won')
                a = 0
                game_on = False
            else:
                if check_tie(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    a = 0
                    break
                else:
                    turn = 'Player2'

        else:
            # cpu turn.
            display_board(theBoard)
            position = cpu_position(theBoard)
            place_marker(theBoard,position,player2)
            
            if check_win(theBoard, player2):
                display_board(theBoard) 
                print('Computer has won')
                a = 0
                game_on = False
            else:
                if check_tie(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    a = 0
                    break
                else:
                    turn = 'Player1'