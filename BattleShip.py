import random
import math

'''
Created on Dec 5, 2022

@author: CCaliboso24
'''

def print_b(board):                                                     
### This function prints the blank board in the beginning of the game
### uses a for loop that prints the board row by row    
    
    for r in board:                                                     #for loop, keeps running until row number exceeds rows within board
       for c in r:                                                      #for loop, keeps running until column number exceeds row length
          print(c,end = " ")
       print()


def player_place(ships):
    
    amount = 4
    
    while amount > 0:
        loop = 1
        
        while loop == 1:
            
            if amount == 1:
                answer = input("\nyou have " + str(amount) + " single dot ship,\nplease input coordinates for 1 ship\n")
            else: 
                answer = input("\nyou have " + str(amount) + " single dot ships,\nplease input coordinates for 1 ship\n")
            
            amount = int(amount)
            
            if amount == 1:
                    loop = 2
            
            if len(answer) != 3:                                            #conditional, if the length of answer is not 3, then loop restarts
                print("2 numbers please")
                loop = 1                                                   
                
            else:                                                           #condtional, else do try except
                
                try:                                                        #try, splitting the answer by comma
                    answer = answer.split(",")
                
                except ValueError:                                          #except, player tries again to to submit proper input
                    print("2 numbers only")
                    loop = 1                                    #recalls player_choice function
                
                r = int(answer[0])                                          #variable, r converts the first number from answer
                c = int(answer[1])                                          #variable, c converts the second number from answer
                
                
                if (r < 0) or (c < 0):                                      #conditional, if (r<0) or (c<0) recall player_choice function
                    print("positive numbers only")
                    loop = 1
                    
                if ((r > 4) or (c > 4)):                                                       #conditional, else    
                    print("coordinates too high")
                    loop = 1
                    
                if (ships[r][c] == "[=]") or (ships[r][c] == "[O]"):
                    print("choose different spot")
                    loop = 1
                
                else: 
                    ships[r][c] = "[=]"
                    amount = amount - 1  
                
    
    return ships
                
def comp_place(ships):
    r = random.randint(0,4)                                             #variable, r is assigned random row number
    c = random.randint(0,4)                                             #variable, c is assigned random column number
    
    if (ships[r][c] == "[=]") or (ships[r][c] == "[O]"):                    #conditional, in coordinates chosen by computer are occupied, computer tries again
        comp_place(ships)
    else:                                                               #else, chosen coordinate is filled with O
        print("\n\ncomputer turn:")
        ships[r][c] = "[=]"
    
    return ships                                                        #return board with added computer choice

def player_choice(pboard):
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
                player_choice(pboard)                                    #recalls player_choice function
            
            r = int(answer[0])                                          #variable, r converts the first number from answer
            c = int(answer[1])                                          #variable, c converts the second number from answer
            
            
            if (r < 0) or (c < 0):                                      #conditional, if (r<0) or (c<0) recall player_choice function
                print("positive numbers only")
                player_choice(pboard)
                
            else:                                                       #conditional, else    
                if ((r > 4) or (c > 4)):
                    print("coordinates too high")
                    player_choice(pboard)
                elif (pboard[r][c] == "[=]") or (pboard[r][c] == "[O]"):
                    print("choose different spot")
                    player_choice(board)
                else:
                    #################3xdas,huda;h 
                    print("\n\nplayer choice:")
                    pboard[r][c] = ""
                    
                loop = 2
                  
                return pboard
    
    
def comp_choice():
    print("hi")

def print_change(board):
    print("hi")
    
def winner_check(board):
    print("hi")

def print_info(turn, guess, ships):
    print("hi")

def main():     

    gametime = 0
    player = 1
    computer = 2
    
    pboard_guess = [["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    
    pboard_ships = [["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]

    cboard_guess = [["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    
    cboard_ship = [["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    
    print("LET'S PLAY BATTLESHIP\n\n")
    
    print("guesses:")
    print_b(pboard_guess)
    print("\n")
    print("ships:")
    print_b(pboard_ships)
    
    pboard_ships = player_place(pboard_ships)
    cboard_ships = comp_place(cboard_ships)
    
    while gametime == 1:
        pboard = player_choice(pboard_guess)
        gametime = winner_check(pboard_guess)
        print_info(player, pboard_guess, pboard_ships)
        print_change(pboard_guess)
        print_change(pboard_ships)
        
        cboard = comp_choice
        gametime = winner_check(cboard)
        print_info(computer, cboard_guess, cboard_ships)
        
    
    
    
    
if __name__ == "__main__":
    main() 