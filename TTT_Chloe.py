import random
import math

'''
Created on Nov 15, 2022
Name: Chloe Caliboso
Date: 12/9/22
Description: allows user to play tic tac toe with computer 
Bugs: none that I know of
Plan: I divided this code into functions and called them all in main()
'''


def print_b(board):                                                     
### This function prints the blank board in the beginning of the game
### uses a for loop that prints the board row by row    
    
    for r in board:                                                     #for loop, keeps running until row number exceeds rows within board
       for c in r:                                                      #for loop, keeps running until column number exceeds row length
          print(c,end = " ")
       print()
  
  
def print_change_b(board, gametime):
### This function takes in the newest board after a player of computer have submitted their turns    
    
    
    if gametime == 1:                                                   #conditional, if gametime == 1 the game is over and must print the final board
    
        for r in board:                                                 #for loop, keeps running until row number exceeds rows within board
            for c in r:                                                 #for loop, keeps running until column number exceeds row length
              print(c,end = " ")
            print()
        end_game()                                                      #call function end_game(), offers to play again or ends game
            
    else:                                                               #conditional, if gametime != 1 then game keeps going
        print('\n')
    
        for r in board:                                                 #for loop, keeps running until row number exceeds rows within board
            for c in r:                                                 #for loop, keeps running until column number exceeds row length
              print(c,end = " ")
            print()
        
  
def player_choice(board):
### this function allows player to choose which spot to mark with X, as well as checks if that spot is valid. if it is not valid, it calls itself 


    loop = 1                                                            #variable, loop is the counter for the while loop below                                                             

    
    while loop == 1:                                                    #while loop, loop == 1:
        answer = input("\nenter row,column:\n")                         #input variable, requests player for the coordinates of their spot
         
        if len(answer) != 3:                                            #conditional, if the length of answer is not 3, then loop restarts
            print("2 numbers please")
            loop = 1                                                    
            
        else:                                                           #condtional, else do try except
            
            try:                                                        #try, splitting the answer by comma
                answer = answer.split(",")
            
            except ValueError:                                          #except, player tries again to to submit proper input
                print("2 numbers only")
                player_choice(board)                                    #recalls player_choice function
            
            r = int(answer[0])                                          #variable, r converts the first number from answer
            c = int(answer[1])                                          #variable, c converts the second number from answer
            
            
            if (r < 0) or (c < 0):                                      #conditional, if (r<0) or (c<0) recall player_choice function
                print("positive numbers only")
                player_choice(board)
                
            else:                                                       #conditional, else another conditional   
                if ((r > 2) or (c > 2)):                                #conditional, if r or c is larger than 2, player must retry
                    print("coordinates too high")
                    player_choice(board)
                elif (board[r][c] == "X") or (board[r][c] == "O"):      #conditional, elif the coordinates chosen by player are already occupied, player must retry
                    print("choose different spot")
                    player_choice(board)
                else:                                                   #conditional, else fill in coordinate with X
                    print("\n\nplayer choice:")
                    board[r][c] = "X"
                    
                loop = 2                                                #end loop
                  
                return board                                            #return board with added player choice
    
def computer_choice(board):
### this functions allows computer to choose random empty spot
    
    r = random.randint(0,2)                                             #variable, r is assigned random row number
    c = random.randint(0,2)                                             #variable, c is assigned random column number
    
    if (board[r][c] == "X") or (board[r][c] == "O"):                    #conditional, in coordinates chosen by computer are occupied, computer tries again
        computer_choice(board)
    else:                                                               #else, chosen coordinate is filled with O
        print("\n\ncomputer turn:")
        board[r][c] = "O"
    
    return board                                                        #return board with added computer choice

def winner_check(board):
### this function checks if either the computer or player has won after each turn
    
    
    if (board[0][0] == "X") and (board[0][1] == "X") and (board[0][2] == "X"):           #conditional, if there is 3 Xs in a horizontal line at the top, player wins
        print("\nYou win!!\n")
        return 1
    
    elif (board[1][0] == "X") and (board[1][1] == "X") and (board[1][2] == "X"):         #conditional, if there is 3 Xs in a horizontal line in the middle, player wins
        print("\nYou win!!\n")
        return 1
    
    elif (board[2][0] == "X") and (board[2][1] == "X") and (board[2][2] == "X"):         #conditional, if there is 3 Xs in a horizontal line at the bottom, player wins
        print("\n You win!!\n")
        return 1
    
    elif (board[0][0] == "X") and (board[1][1] == "X") and (board[2][2] == "X"):         #conditional, if there is 3 Xs in a diagonal line top left bottom right, player wins
        print("\nYou win!!\n")
        return 1
    
    elif (board[0][2] == "X") and (board[1][1] == "X") and (board[2][0] == "X"):         #conditional, if there is 3 Xs in a diagonal line top left bottom right, player wins
        print("\nYou win!!\n")
        return 1
    
    elif (board[0][0] == "X") and (board[1][0] == "X") and (board[2][0] == "X"):         #conditional, if there is 3 Xs in a vertical line in column zero, player wins
        print("\nYou win!!\n")
        return 1
    
    elif (board[0][1] == "X") and (board[1][1] == "X") and (board[2][1] == "X"):         #conditional, if there is 3 Xs in a vertical line in column zero, player wins
        print("\nYou win!!\n")
        return 1
    
    elif (board[0][2] == "X") and (board[1][2] == "X") and (board[2][2] == "X"):         #conditional, if there is 3 Xs in a vertical line in column zero, player wins
        print("\nYou win!!\n")
        return 1
    
    
    
    elif (board[0][0] == "O") and (board[0][1] == "O") and (board[0][2] == "O"):        #conditional, if there is 3 Os in a horizontal line at the top, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[1][0] == "O") and (board[1][1] == "O") and (board[1][2] == "O"):        #conditional, if there is 3 Os in a horizontal line in the middle, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[2][0] == "O") and (board[2][1] == "O") and (board[2][2] == "O"):        #conditional, if there is 3 Os in a horizontal line at the bottom, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[0][0] == "O") and (board[1][1] == "O") and (board[2][2] == "O"):        #conditional, if there is 3 Os in a diagonal line top left bottom right, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[0][2] == "O") and (board[1][1] == "O") and (board[2][0] == "O"):        #conditional, if there is 3 Os in a diagonal line top left bottom right, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[0][0] == "O") and (board[1][0] == "O") and (board[2][0] == "O"):        #conditional, if there is 3 Os in a vertical line in column zero, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[0][1] == "O") and (board[1][1] == "O") and (board[2][1] == "O"):        #conditional, if there is 3 Os in a vertical line in column zero, computer wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[0][2] == "O") and (board[1][2] == "O") and (board[2][2] == "O"):        #conditional, if there is 3 Xs in a vertical line in column zero, player wins
        print("\nComputer wins!!\n")
        return 1
    
    elif (board[0][0] != ".") and (board[0][1] != ".") and (board[0][2]) != "." and (board[1][0] != ".") and (board[1][1] != ".") and (board[1][2] != ".") and (board[2][0] != ".") and (board[2][1] != ".") and (board[2][2] != "."):
        print("no one wins")                                                            #conditional, if all coordinates are taken yet no one has won, tie
        return 1
    
    else:
        return 0                                                                                    
    
def end_game():
### this function ends game and also asks player if they want to play again
    
    
    ask = input("you wanna play again??? yes or no.\n")         #variable input, ask asks player if they want to play again
        
    if ask == (("yes") or ("YES") or ("Yes")):                  #conditional, if ask is any of these 3 variations of yes, call main
        main()
    elif ask == (("no") or ("NO") or ("No")):                   #conditional, if ask is any of these 3 variations of no, print bye and end
       print("bye")
    else:                                                       #conditional, else is invalid input, user must try again
        print("invalid")
        end_game()
    
def main():

    gametime = 0                                                #variable, decided by winner_check() 
    
    print("let's play Tic Tac Toe\n")

    board = [[".",".","."], [".",".","."], [".",".","."]]       #variable, board array that stores game board
    
    print_b(board)                                              #function
    
    while gametime == 0:                                        #while loop, game runs while gametime == 0
        board = player_choice(board)                            #variable, board manipulated by playerchoice()
        gametime = winner_check(board)                          #variable, winnercheck() determining gametime
        print_change_b(board, gametime)                         #function
        
        board = computer_choice(board)                          #variable, board manipulated by computer_choice()    
        gametime = winner_check(board)                          #variable, winnercheck() determining gametime
        print_change_b(board, gametime)                         #function
        
        

        

if __name__ == "__main__":
    main()