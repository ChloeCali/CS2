"""
Name: Ellie Hochberg, Chloe Caliboso, Steve Paul
Date: Oct 11, 2022
Description: This program manipulates strings. Given a character string and a list of functions that operate on strings, the resulting string is calculated.
Bugs: No bugs.
Log: Submitted on
Plan: 
    1) Take input
    2) Split input at the slash
    3) Split at dash
    4) Call the function
    5) Return manipulated string
"""


def leftShift(num,text):
    """
    Shifts all the characters of the string 'num' places to the left. Delete the leftmost 'num' characters and replace with #'s
    Arguments: 
        num: the number of places the string will be shifted to the left
        text: the string that contains the word being manipulated 
    Returns: 
        finalWord: the resulting string
    """
    

    wrd = []                                    #wrd array will hold all letters of a word separate
    
    cnt1 = 0                                     #cnt1 is the counter for the while loop (while (cnt1 < len(word))
    while cnt1 < len(text):
        char = text[cnt1]
        wrd.append(char)
        cnt1 = cnt1 + 1
    
    #This while loop places all characters in the word into the wrd array
    
    

    cnt2 = 0                                    #cnt2 is the counter for the while loop (while (cnt2 < num)
    while (cnt2 < num):
        wrd.pop(0)
        cnt2 = cnt2 + 1
    
    #This while loop deletes the specific amount of characters that are pushed out of the array  
    
    
    
    cnt3 = 0                                     #cnt3 is the counter for the while loop (while (cnt3 < num)
    while (cnt3 < num):
        wrd.append("#")
        cnt3 = cnt3 + 1
    '''
    This while loop appends the specific amount of # at the end  
    '''

    text = "".join(wrd)                    #finalWord is the wrd array converted to a string
    return text
    
    

def rightShift(num, text):
    """
    Shifts all the characters of the string 'num' places to the right. Delete the rightmost 'num' characters and replace with #'s
    Arguments: 
        num: the number of places the string will be shifted to the right
        text: the string being manipulated
    Returns:
        word: the resulting string
    """

    cnt = 0  # the counter for the while loop
    end = len(text)
    end = end - num
    word = text[0:end]

    while cnt < num:  # Determining how many hashtags it needs to add to the front so it runs the loop that many times

        word = "#" + word  # Adds the hashtags that removed the letters to the beginning of the word
        cnt += 1
        text = word
    return text  # Returns the finished word



def leftCirc(num, text):
    """
    Circulates the leftmost 'num' characters to the right hand side of the string
    Arguments: 
        num: the number of characters being moved to the right hand side
        text: the string that contains the word being manipulated 
    Returns: 
        text: the resulting string
    """
    circ = text[num:]                       #all the characters 'num' and after
    text = text[:num]                       #all the characters before 'num'
    text = circ + text                      #resulting string
    return text



def rightCirc(num, text):
    """
    Circulates the rightmost 'num' characters to the left hand side of the string
    Arguments: 
        num: the number of characters being moved to the left hand side
        text: the string that contains the word being manipulated 
    Returns: 
        text: the resulting string
    """
    num = len(text)-num
    circ = text[:num]                     #all the characters before 'num'
    text = text[num:]                     #all the characters 'num' and after
    text = text + circ                   #resulting string
    return text


def subCirc(position, length, num, direction, text):
    """
    Circulates the sub-string starting in a position of 'position' with a length of 'length', 'num' characters, in the direction, 'direction'
    Arguments:
        position: starting position
        length: length of sub-string
        num: number of characters
        direction: direction it's going in
        text: the string that contains the word being manipulated
    Returns:
        text: resulting string
    """
    circ = []                                           #This array holds the letters that will be circulated and inserted in the final 
    wrd = []                                            #This array holds all the letters of text
    first = []                                          #This array holds the letters before the selected characters from the text
    second = []                                         #This array holds the letters after the selected characters from the text

    if num >= length:
        while num >= length:
            num = num - length                          #conditional reduces num so the rotation amount is less than the length
    
    position = position - 1                             #Position variable takes the position and properly formats the number for arrays by subtracting 1
    trueLength = position + length                      #trueLength takes the length and formats the number in termns of the wrd array
    letters = text[position:trueLength]                 #letters will hold all letters selected to circulate in the form of a string
  
    cnt1 = 0                                            #cnt1 is the counter for the loop "for letter in text"
    for letter in text:                                 #This loop appends all letters from text into the wrd array 
        wrd.append(text[cnt1])
        cnt1 = cnt1 + 1                                 

    cnt2 = 0                                            #cnt2 is the counter for the loop "while cnt2 < len(letters)"
    while cnt2 < len(letters):                          #This loop appends all selected letters from text to be circulated in the circ array
        circ.append(letters[cnt2])
        cnt2 = cnt2 + 1 
    
    
    cnt3 = 0                                             #cnt3 is the counter for the loop "while cnt3 < position"
    while cnt3 < position:                               #this loop appends the letters before the selected characters in text to first = []
        first.append(wrd[cnt3])
        cnt3 = cnt3 + 1
        
    
    cnt4 = 0                                             #cnt4 is the counter for the loop "while cnt4 < len(wrd[trueLength:])"
    while cnt4 < len(wrd[trueLength:]):                  #this loop appends the letters after the selected characters from text to second = []
        second.append(wrd[trueLength + cnt4])
        cnt4 = cnt4 + 1
    
    
    cnt5 = 0                                            #cnt5 is the counter for the 4 the loops below 
    changed = []                                        #changed = array that holds the letters that stick together after circulation
    if direction == "L":                                #conditional will circulate letters to the left
        while (cnt5 < num):                             #This loop appends the characters that stick together after circulation to changed = []
            changed.append(circ[cnt5])
            cnt5 = cnt5 + 1
        cnt5 = 0                                        #resetting cnt5 for while loop "while (num < length)"
        while (num < length):                           #This loop shifts the character/s that change then it joins it with changed = []
            circ[cnt5] = circ[length - 1]
            cnt5 = cnt5 + 1
            num = num + 1
        circ = circ[:cnt5] + changed
        
               
    elif direction == "R":                              #conditional will circulate letters to the left
        while cnt5 < (length - num):                    #This loop appends the characters that stick together after circulation to changed = []
            changed.append(circ[cnt5])
            cnt5 = cnt5 + 1
        cnt5 = 0                                        #resetting cnt5 for while loop "while (num < length)"
        while (num < length):
            circ[cnt5] = circ[length - 1]
            cnt5 = cnt5 + 1
            num = num + 1
        circ = circ[cnt5:] + changed                    #This loop shifts the character/s that change then joins it with changed = []
        
    
    pOne = "".join(first)                               #pOne = conversion of the "first" array to string
    pTwo = "".join(circ)                                #pTwo = conversion of the "circ" array to string
    pThree = "".join(second)                            #pThree = conversion of the "second" array to string
    text =  pOne + pTwo + pThree                         #text = the combinations of pOne + pTwo + pThree
    return text



def reverseString(position, length, text):
    """
    This function reverses the middle letters based on position and the length
    Arguments:
        position: starting position
        length: length of string being reversed
        text: the string that contains the word being manipulated 
    Returns:
        text: A string which is reversed of the part 
    """
    output = "" 
    string = text
    before_reverse = text[:position-1]                #Keeping letters before the reverse letters
    after_reverse = text[position + length -1:]       #Keeping letters after the reverse letters the same
    for i in range(len(string)-1, -1, -1):              #Reversing the middle letters
        output = output + string[i]
    position = position +1
    end = position + length
    output = output[position:end]
   
    text = before_reverse + output + after_reverse
    
    return text
    


def main():
    """
    Calculate resulting string given a character string and a list of functions
    Arguments: 
        N/A
    Returns: 
        N/A
    """
    
    data = "LS-1/LC-3/MC-543L/MEMORIAL"
    data = data.split("/")                            #split string at the /
    data_num = len(data)                              #length of the string
    
    text = data[-1]                                    #the word that will be manipulated 
    
    count = 0
    while count < data_num:
        command = data[count]    
        command = command.split("-")                  #split at the -
        function = command[0]                          #function getting called is the 0th term
        
        if function == "LS":                              #leftShift function
            num = int(command[-1])                        #num is the -1th term
            text = leftShift(num, text)                    #call function
           
        elif function == "RS":                            #rightShift function
            num = int(command[-1])                          #num is the -1th term
            text = rightShift(num, text)                   #call function
          
        elif function == "LC":                             #leftCirc function
            num = int(command[-1])                          #num is the -1th term
            text = leftCirc(num, text)                         #call function
           
        elif function == "RC":                             #rightShift function
            num = int(command[-1])                          #num is the -1th term
            text = rightCirc(num, text)                       #call function
            
        elif function == "MC":                                         #subCirc function
            func_commands = command[-1]                                 # function commands 
            position = int(func_commands[-4])                           #starting position
            length = int(func_commands[-3])                              #length
            num = int(func_commands[-2])                                 #num: num of characters
            direction = str(func_commands[-1])                          #what direction it's going in
            text = subCirc(position, length, num, direction, text)        #call function
         
        elif function == "REV":                                     #reverseString function
            func_commands = command[-1]               
            position = int(func_commands[-2])                        #position
            length = int(func_commands[-1])                           #length   
            text = reverseString(position, length, text)              #call function
             
        count = count + 1
        
    print(text)
    
if __name__ == "__main__":
    main()