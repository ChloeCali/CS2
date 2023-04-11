'''
Created on Feb 1, 2023

@author: CCaliboso24    
'''
   


def main():  
 
    D = dict()                                                                              #variable, D = dictionary
    L = list()                                                                              #variable, L = list

    f = open('C:\\Users\\ccaliboso24\\Desktop\\mbox-short.txt', 'r')                        #variable, f = opened text file

    for line in f:                                                                          #for loop, goes through all lines in text file
        
        words = line.split()                                                                #variable, words = list of the words in each line
        
        if bool(words):                                                                     #conditional, checks if theres characters in the line

            wrd = words[0]                                                                  #varaible, wrd = first word in line             


            if wrd.upper() == "FROM":                                                       #conditional, if line starts with From, continue code
                if words[1] not in D:                                                       #conditional, if the second word in the line is not in D, put it in D and assign it value of one
                    D[words[1]] = 1
                else:                                                                       #coditional, else: increase word's value by 1
                    D[words[1]] = D[words[1]] + 1


            elif wrd.upper() == "FROM:":                                                    #conditional, elif line starts with From:, continue code
                if words[1] not in D:                                                       #conditional, if the second word in the line is not in D, put it in D and assign it value of one
                    D[words[1]] = 1
                else:                                                                       #coditional, else increase word's value by 1
                    D[words[1]] = D[words[1]] + 1           
            
    

            elif len(words) < 2:                                                            #coditional, elif length of word is 1, continue
                continue
            else:                                                                           #conditional, else continue
                continue
            
        else:                                                                               #conditional, else continue
            continue
        
    for key, val in list(D.items()):                                                        #For loop, for all items in D, append to L
        L.append((val, key))

    L.sort(reverse=True)                                                                    #sort L in reverse order



    w = L[0]                                                                                #variable, w = first element in L
    w = str(w)                                                                              #variable, convert w to string
    w = w.split()                                                                           #variable, split w 

    w1 = [0]                                                                                #variable, w1 = list with 0
    w2 = [1]                                                                                #variable, w2 = list with 1
    
    for letter in w[0]:                                                                     #for loop, goes through every letter in the first word of the line and appends it to w1
        w1.append(letter)   

    for letter in w[1]:                                                                     #for loop, goes through every letter in the second word of the line and appends it to w2
        w2.append(letter)

    del(w1[0])                                                                              #delete first character in w1
    del(w1[0])                                                                              #delete first character in w1
    del(w1[len(w1) - 1])                                                                    #delete last character in w1

    del(w2[0])                                                                              #delete first character in w2
    del(w2[0])                                                                              #delete first character in w2
    del(w2[len(w2) - 1])                                                                    #delete last character in w2
    del(w2[len(w2) - 1])                                                                    #delete last character in w2

    w2 = "".join(w2)                                                                        #convert w2 to string
    w1 = "".join(w1)                                                                        #convert w1 to string

    print(w1 + ", " + w2)                                                                   #print final output





if __name__ == "__main__":
    main() 
    
