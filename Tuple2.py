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

            try:                                                                            #try
                colon = words[5].find(":")                                                  #variable, find the index of the colon in the 6th word of the line
                time = words[5][:colon]                                                     #variable, assign time to all chars before the colon in the 6th word                    

                if time not in D:                                                           #conditional, if time not in D, put in D and assign value of 1
                    D[time] = 1
                else:                                                                       #conditional, else, increase time value by one
                    D[time] += 1
            
            except IndexError:                                                              #except, continue
                continue
            
        else:                                                                               #conditional, else continue
            continue
    
    
    for key, val in list(D.items()):                                                        #for all elements in D, append to L only if key = 1 to 24


        if key == "0" or key == "01" or key == "02" or key == "03" or key == "04" or key == "05" or key == "06" or key == "07" or key == "08" or key == "09" or key == "10" or key == "11" or key == "12" or key == "13" or key == "14" or key == "15" or key == "16" or key == "17" or key == "18" or key == "19" or key == "20" or key == "21" or key == "22" or key == "23" or key == "24":
            L.append((key, val))
        else:
            continue

    L.sort()                                                                                #sort numerically by key


    for key, val in L:                                                                      #print each element of L
        print(key,val)

if __name__ == "__main__":
    main() 
    
