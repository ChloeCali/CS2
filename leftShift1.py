
'''
Created on Oct 13, 2022

@author: CCaliboso24
'''

def leftShift(X):
    nums = []                                   #nums is the array that stores the numbers
    wrds = []                                   #wrds is the array that stores the letters/word
    
    
    cnt1 = 0                                    #cnt 1 is the counter for the for loop (for letter in X)
    for letter in X:
        

        char = X[cnt1]                          #char represents the the characters in the input 
        
        try: 
            char = int(char)
            cnt1 = cnt1 + 1
            char = str(char)
            nums.append(char)    
        except:
            wrds.append(char)
            cnt1 = cnt1 + 1 
        
        '''
        this try except organizes the characters in the input by letter and number 
        '''
                            

    cnt2 = 0                                    #cnt2 is the counter for the for loop (for letter in wrds)
    for letter in wrds:
    
        if wrds[cnt2] == " ":
            wrds.pop(cnt2)
            cnt2 = cnt2 + 1                     #This conditional deletes all spaces in the wrds array
    
    realNum = "".join(nums)                     #real num is the nums array converted to a combines string
    
    realNum = int(realNum)                      #the realNum conversion of string to number
    
    if realNum > len(wrds):
        print("number must be smaller than the length of the word, try again")
        nums.clear()
        wrds.clear()
        main()                                  #this conditional makes sure the number is less than the length of the word
         
    
    cnt3 = 0                                    #cnt3 is the counter for the while loop (while (cnt3 < realNum)
    while (cnt3 < realNum):
        wrds.pop(0)
        cnt3 = cnt3 + 1
    '''
    This while loop deletes the specific amount of characters that are pushed out of the array  
    '''
    
    
    cnt4 = 0
    while (cnt4 < realNum):
        wrds.append("#")
        cnt4 = cnt4 + 1
    '''
    This while loop appends the specific amount of # at the end  
    '''
    
    
    finalWord = "".join(wrds)                   #finalWord is the wrds array converted to a joined string
    print(finalWord)
    
    
    
    
    
def main():
    
    leftShift(input("enter X and word:\n"))
    
if __name__ == '__main__':
    main()