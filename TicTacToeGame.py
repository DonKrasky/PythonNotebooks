# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 20:05:20 2021

@author: dkras
"""

#Game script, run to play game
from IPython.display import clear_output

#-------------------------Functions for use in game-------------------

#Returns an empty player move list
def new_board():
    board = []
    for i in range(10):
        board.append(' ')
    return board

#print game board with current moves
def print_board(moves):
    print('Position Labels:' + '        ' + 'Current Game:')
    print('     ' + '7' + '|' + '8' + '|' + '9' + '                 ' + moves[6] + '|' + moves[7] + '|' + moves[8])
    print('     ' + '-----' + '                 ' + '-----')
    print('     ' + '4' + '|' + '5' + '|' + '6' + '                 ' + moves[3] + '|' + moves[4] + '|' + moves[5])
    print('     ' + '-----' + '                 ' + '-----')
    print('     ' + '1' + '|' + '2' + '|' + '3' + '                 ' + moves[0] + '|' + moves[1] + '|' + moves[2])
    
#Return True or False if a "win" is on the board
def winning_board(board):
    if (board[0] in ['X','O']) and (board[0] == board[1]) and (board[1] == board[2]):
        return True
    if (board[0] in ['X','O']) and (board[0] == board[4]) and (board[4] == board[8]):
        return True
    if (board[0] in ['X','O']) and (board[0] == board[3]) and (board[3] == board[6]):
        return True
    if (board[3] in ['X','O']) and (board[3] == board[4]) and (board[4] == board[5]):
        return True
    if (board[6] in ['X','O']) and (board[6] == board[4]) and (board[4] == board[2]):
        return True
    if (board[6] in ['X','O']) and (board[6] == board[7]) and (board[7] == board[8]):
        return True
    if (board[7] in ['X','O']) and (board[7] == board[4]) and (board[4] == board[1]):
        return True
    if (board[8] in ['X','O']) and (board[8] == board[5]) and (board[5] == board[2]):
        return True
    else:
        return False

#---------------------------Core game logic----------------------------
    
#Welcome message and variable initialization

keep_playing = True
board = new_board()
player = None
move = None

print('Welcome to tic-tac-toe!')
player = input('Choose X or O:').upper()

#Check for valid player character, ask again if not valid.
while player not in ['X','O']:
    clear_output()
    player = input("This isn't that hard, choose X or O:").upper()

#Main game loop
while keep_playing:
    #Prompt for player move and store
    while move not in ['1','2','3','4','5','6','7','8','9']:
        clear_output()
        print("          This is Tic-Tac-Toe")
        print("               " + player + ' plays')
        print_board(board)
        
        #Check for previous over-write attempt
        if move == 'no':
            print("Position occupied, move invalid.")
            move = None
            
        #Check for invalid selection
        if move == 'cant':
            print("Move invalid.")
            move = None
        
        #Accept players move
        move = input("Make your move (1-9):")
        
        #Over-write not allowed, que error message for invalid input
        if move in ['1','2','3','4','5','6','7','8','9']:
            if board[int(move)-1] in ['X','O']:
                move = 'no'
        else:
            move = 'cant'
    
    #Update board with move
    board[int(move)-1] = player
    move = None
    
    #Check for win 
    if winning_board(board):
        chirp = None
        while chirp not in ['Y','N']:
            clear_output()
            print("               " + player + ' Wins!')
            print_board(board)
            
            #Invalid selection message
            if chirp != None:
                print('Invalid selection.')
                chirp = None
            
            chirp = input('Play again? (Y/N):').upper()
            
        if chirp == 'N':
            keep_playing = False
            break
        else:
            keep_playing = True
            board = new_board()
            player = None
            move = None
            
            print('Welcome to tic-tac-toe!')
            player = input('Choose X or O:').upper()
            
            #Check for valid player character, ask again if not valid.
            while player not in ['X','O']:
                clear_output()
                player = input("This isn't that hard, choose X or O:").upper()
                
            continue
    
    #Change Player
    if player == 'X':
        player = 'O'
    else:
        player = 'X'