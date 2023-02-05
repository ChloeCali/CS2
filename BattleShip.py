'''
Created on Dec, 16, 2022
Name: Chloe Caliboso
Date: Feb, 3, 2023
Description: Play battleship with computer
Bugs: none
'''
import random

def print_b(board):                                                     
### print_b(board) function prints the blank board in the beginning of the game
### uses a for loop that prints the board row by row    




    for r in board:                                                             #for loop, keeps running until row number exceeds rows within board
       for c in r:                                                              #for loop, keeps running until column number exceeds row length
          print(c,end = " ")                                                    #prints board element by element
       print()


def player_place(ships):                                                
### player_place(ships) function takes player input of coordinates and uses that as ship placements in the pboard_ships array
### also troublshoots input to certify proper format


    amount = 4                                                                  #variable, used to stop loop after 4 runs
    
    while amount > 0:                                                           #while loop, lets player place 4 ships
        loop = 1
        
        while loop == 1:                                                        #while loop, makes sure player input is valid
            
            answer = input("\nyou have " + str(amount) + " single dot ship,\nplease input coordinates for 1 ship\n")    #variable - input, asks player for coordinates and counts how many ships left
            
            amount = int(amount)                                                #variable - converts input back to integer
            
            if amount == 1:                                                     #conditional: ends loop after 4 ships have been place
                    loop = 2                                                
            
            if len(answer) != 3:                                                #conditional, if the length of answer is not 3, then loop restarts
                print("2 numbers please")
                loop = 1                                                   
                
            else:                                                               #condtional, else do try except
                
                try:                                                            #try, splitting the answer by comma
                    answer = answer.split(",")
                
                except ValueError:                                              #except, player tries again to to submit proper input
                    print("2 numbers only")
                    loop = 1                                                    #recalls player_choice function
                
                r = int(answer[0])                                              #variable, r converts the first number from answer
                c = int(answer[1])                                              #variable, c converts the second number from answer
                
                try:                                                            #try, multiple forms of troubl shooting
                    if (r < 0) or (c < 0):                                      #conditional, if (r<0) or (c<0) restart loop
                        print("positive numbers only")
                        loop = 1
                        
                    elif ((r > 4) or (c > 4)):                                  #conditional, elif ((r > 4) or (c > 4)) restart loop                              
                        print("coordinates too high")
                        loop = 1
                        
                    elif (ships[r][c] == "[=]") or (ships[r][c] == "[O]"):      #conditional, elif (ships[r][c] == "[=]") or (ships[r][c] == "[O]") restart loop
                        print("choose different spot")
                        loop = 1
                    
                    else:                                                       #conditional, else, assign ship placement and change amount
                        ships[r][c] = "[=]"
                        amount = amount - 1  
                
                except:                                                         #except: print player suggestion                
                    print("please use format n,n")  
                    continue
                
    
    return ships

                
def comp_place(ships):
### comp_place(ships) function assigns random ship placements on cboard_ships array 



    loop = 1

    while loop < 5:
        r = random.randint(0,4)                                             #variable, r is assigned random row number
        c = random.randint(0,4)                                             #variable, c is assigned random column number
        
        if (ships[r][c] == "[=]") or (ships[r][c] == "[O]"):                #conditional, in coordinates chosen by computer are occupied, computer tries again
            continue
        else:                                                               #else, chosen coordinate is filled with O
            ships[r][c] = "[=]"
            loop = loop + 1
        
    return ships                                                            #return board with added computer choice

def player_choice(stat, pguess, cships):
    loop = 1                                                                #variable, loop is the counter for the while loop below                                                             

    
    while loop == 1:                                                        #while loop, loop == 1:
        answer = input("\nenter row,column guess:\n")                       #input variable, requests player for the coordinates of their spot
         
        if len(answer) != 3:                                                #conditional, if the length of answer is not 3, then loop restarts
            print("2 numbers please")
            loop = 1                                                    
            
        else:                                                               #condtional, else do try except
            
            try:                                                            #try, splitting the answer by comma
                answer = answer.split(",")
            
            except ValueError:                                              #except, player tries again to to submit proper input
                print("2 numbers only")
                player_choice(stat, pguess, cships)                         #recalls player_choice function

            try:
                r = int(answer[0])                                          #variable, r converts the first number from answer
                c = int(answer[1])                                          #variable, c converts the second number from answer
            
            except ValueError:                                              #except, restart function                    
                print("2 numbers only")
                player_choice(stat, pguess, cships)                         
            

            if ((r > 4) or (c > 4)):                                        #conditional, if ((r > 4) or (c > 4)) retsart function
                print("coordinates too high")
                player_choice(stat, pguess, cships)

            elif (cships[r][c] == "[X]") or (cships[r][c] == "[O]"):        #conditional, elif (cships[r][c] == "[X]") or (cships[r][c] == "[O]") retsart function
                print("choose different spot")
                player_choice(stat, pguess, cships)
                
            else:                                                           #condtition, else: assign hit("[X]") or miss("[O]") values in cboard_ships array
                if cships[r][c] == "[=]":
                    cships[r][c] = "[X]"
                    pguess[r][c] = "[X]"
                    stat = 1
                
                elif cships[r][c] == "[ ]":
                    cships[r][c] = "[O]"
                    pguess[r][c] = "[O]"
                    stat = 2
                        
                loop = 2
                
            return stat, pguess, cships

    
    
def comp_choice(stat, cguess, pships):
### comp_chouce(stat, cguess, pships) function guesses random coordinates on player's board


    loop = 1                                                                #variable, c is assigned random column number
    
    while loop == 1:    
        r = random.randint(0,4)                                             #variable, r is assigned random row number
        c = random.randint(0,4)   
        
        if (pships[r][c] == "[X]") or (pships[r][c] == "[O]"):              #conditional, in coordinates chosen by computer are occupied, computer tries again
            continue 
        else:                                                               #else, assign chosen coordinate with hit("[X]") or miss("[O]") values in pboard_ships array
            if pships[r][c] == "[=]":
                pships[r][c] = "[X]"
                cguess[r][c] = "[X]"
                stat = 1
                loop = 2
    
            elif pships[r][c] == "[ ]":
                pships[r][c] = "[O]"
                cguess[r][c] = "[O]"
                stat = 2
                loop = 2
                
    return stat, cguess, pships
    

def winner_check(turn, guess):
### winner_check(turn, guess) function takes in every coordinate of a board and checks if the player or computer has won


    winning_count = 0                                                       #variable, counts sunken ships
    r = 0                                                                   #variable, r = row
    c = 0                                                                   #variable, c = column

    while r < 5:                                                            #while loop, cycles through every coordinate of board
        c = 0                                           
        while c < 5:
            if guess[r][c] == "[X]":                                        #conditional, if guess[r][c] == "[X]" add 1 to winning_count
                winning_count = winning_count + 1
                c = c + 1
            else: 
                c = c + 1
        r = r + 1
    
    
    
    if winning_count == 4:                                                  #conditional, if winning_count == 4, assign different numbers to endings depending if player or computer reached winning_count = 4
        if turn == 1:
            ending = 1
            
        elif turn == 2:
            ending = 2
        
    else:                                                                   #else: game doesn't end
        ending = 0
    
    return ending



def print_info(ending, turn, stat, gametime):
### print_info(ending, turn, stat, gametime) function takes in ending, turn, status of board, and gametime and outputs moves left and move outcome


    if turn == 1:   #turn 1 = player                                        #conditional, if turn == 1, output player's move's outcome
        if stat == 1:                                                       #conditional, if stat == 1, outcome is player sunk computer's ship
            print("\nyou sunk my battleship !\n")
        elif stat == 2:                                                     #conditonal, elif state == 2, oucome is player missed computer ship
            print("you missed !")



    elif turn == 2: #turn 2 = computer                                      #conditional, if turn == 1, output computer's move's outcome
        if stat == 1:                                                       #conditional, if stat == 1, outcome is computer sunk player's ship
            print("\nmy turn:\nI sunk your battleship !\n")

        elif stat == 2:                                                     #conditional, if stat == 2, outcome is computer missed player's ship
            print("\nmy turn:\nI missed !\n")


    if ending == 1:                                                         #conditional, if ending == 1, player wins
        print("\nYou win !\n")

    elif ending == 2:                                                       #conditional, if ending == 2, player loses
        print("\nYou lose !\n")
    
    else:                                                                   #conditional, else: game goes on and prints moves left
        print("\nyou have " + str(9 - gametime) + " moves left\n")
    



  

   
def main():  
    
    pboard_guess = [["[ ]","[ ]","[ ]","[ ]","[ ]"],                        #variable, array pboard_guess stands for player's board of guesses
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    
    pboard_ships = [["[ ]","[ ]","[ ]","[ ]","[ ]"],                        #variable, array pboard_ships stands for player's board of ships
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]

    cboard_guess = [["[ ]","[ ]","[ ]","[ ]","[ ]"],                        #variable, array cboard_guess stands for computer's board of guesses
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    
    cboard_ships = [["[ ]","[ ]","[ ]","[ ]","[ ]"],                        #variable, array cboard_ships stands for computer's board of ships
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"], 
              ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    
    print("LET'S PLAY BATTLESHIP\n\n")
    
    print("[=] = ship \n[X] = sunken ship \n[O] = missed guess\n\n")
    print("\n you have 10 moves to win\n")
    

    
    print("guesses:")
    print_b(pboard_guess)                                                   #calls print_b function to print player's guess board
    print("\n")
    print("ships:")              
    print_b(pboard_ships)                                                   #calls print_b function to print player's ships board
    pboard_ships = player_place(pboard_ships)                               #reassigns pboard_ships value by calling player_place(ships) function
    print("\nships:\n")
    print_b(pboard_ships)                                                   #calls print_b function to print updated player's ship board
    cboard_ships = comp_place(cboard_ships)                                 #reassigns cboard_ships value by calling comp_place(ships) function
    
    gametime = 0                                                            #variable, gametime counts number of moves
    player = 1                                                              #variable, player is represented by 1 when used with turn variable
    comp = 2                                                                #variable, computer is represented by 2 when used with turn variable
    ending = 0                                                              #variable, ending = 0 means game goes on, ending = 1 means player won, ending = 2 means player lost
    pstatus = 0                                                             #variable, pstatus = 1 means player sunk ship, pstatus = 2 means player missed
    cstatus = 0                                                             #variable, cstatus = 1 means computer sunk ship, cstatus 2 means computer missed

    while gametime < 10:                                                    #while loop, player only has 10 moves to win or lose
        
        pstatus, pboard_guess, cboard_ships = player_choice(pstatus, pboard_guess, cboard_ships)            #reassigns pstatus, pboard_guess, cboard_ships by calling player_choice function
        ending = winner_check(player, pboard_guess)                                                         #reassigns ending by calling winner_check function (checks if anyone has won)
        print_info(ending, player, pstatus, gametime)                                                       #calls print_info function to output statuses and if anyone has won or lost
        if ending != 0:                                                                                     #conditional, if player has won, break loop
            break  
        
        cstatus, cboard_guess, pboard_ships = comp_choice(cstatus, cboard_guess, pboard_ships)              #reassigns cstatus, cboard_guess, pboard_ships by calling player_choice function
        ending = winner_check(comp, cboard_guess)                                                           #reassigns ending by calling winner_check function (checks if anyone has won)
        print_info(ending, comp, cstatus, gametime)                                                         #calls print_info function to output statuses and if anyone has won or lost
        if ending != 0:                                                                                     #conditional, if computer has won, break loop
            break 
        
        print("\nguesses:\n")
        print_b(pboard_guess)                                                                               #calls print_b function to print player's guess board
        print("\nships:\n")
        print_b(pboard_ships)                                                                               #calls print_b function to print player's ship board
        
        gametime = gametime + 1                                                                     

    print("\ntie, no one wins!")                                                                            #outcome if no one has won or lost
    
    
    
if __name__ == "__main__":
    main() 
    
