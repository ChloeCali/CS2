'''
Created on Feb 1, 2023

@author: CCaliboso24    
'''
   


def main():  
 
    D = dict()                                                                              #variable, D = dictionary
    L = list()                                                                              #variable, L = list
    cnt = 0                                                                                 #variable, cnt
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #variable list, abc = alphabet
    
    f = open('C:\\Users\\ccaliboso24\\Desktop\\mbox-short.txt', 'r')                        #variable, f = opened text file


    for line in f:                                                                          #for loop, goes through all lines in text file
        
        words = line.split()                                                                #variable, words = list of the words in each line
        
        if bool(words):                                                                     #conditional, checks if theres characters in the line

            for word in words:                                                              #for loop, goes through every word in line
                for letter in word:                                                         #for loop, goes through every letter per word in line
                    cnt = cnt + 1                                                           #increase cnt value by 1
                    if letter not in D:                                                     #conditional, if character not a letter, pass
                        if letter not in abc:
                            pass
                        else:                                                               #conditional, else put letter in D and assign value of 1
                            D[letter] = 1
                    else:                                                                   #conditional, else conditional
                        if letter not in abc:                                               #conditional, if char not in abc, pass
                            pass
                        else:                                                               #conditional, else, increase value of letter by 1 in D
                            D[letter] = D[letter] + 1

    
    
    for key, val in list(D.items()):                                                        #for all elements in D, append to L
        L.append((val, key))
        

    L.sort(reverse=True)                                                                    #sort in r


    for key, val in L:
        print(key,val)

if __name__ == "__main__":
    main() 
    
