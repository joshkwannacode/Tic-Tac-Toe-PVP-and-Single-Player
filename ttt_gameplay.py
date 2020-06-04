"""
Simple tic tac toe game that has an option to play pvp or single player

"""
import ttt_func #functions from the ttt_func.py

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