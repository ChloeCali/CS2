'''
Created on Oct 25, 2022

@author: CCaliboso24
'''
def subCirc(position,length,num,direction,text):

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
        circ[:] = circ[:cnt5] + changed
      
               
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
    text =  pOne + pTwo + pThree                   #finalWord = the combinations of pOne + pTwo + pThree
    print(text)


def main():

    
if __name__ == '__main__':
    main()
