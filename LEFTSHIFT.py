
'''
Created on Oct 13, 2022

@author: CCaliboso24
'''
from turtledemo.nim import computerzug

def leftShift(num,word):

    wrd = []                                    #wrd array will hold all letters of a word separate
    
    cnt1 = 0                                     #cnt1 is the counter for the while loop (while (cnt1 < len(word))
    while cnt1 < len(word):
        char = word[cnt1]
        wrd.append(char)
        cnt1 = cnt1 + 1
    '''
    This while loop places all characters in the word into the wrd array
    '''
    

    cnt2 = 0                                    #cnt2 is the counter for the while loop (while (cnt2 < num)
    while (cnt2 < num):
        wrd.pop(0)
        cnt2 = cnt2 + 1
    '''
    This while loop deletes the specific amount of characters that are pushed out of the array  
    '''
    
    
    cnt3 = 0                                     #cnt3 is the counter for the while loop (while (cnt3 < num)
    while (cnt3 < num):
        wrd.append("#")
        cnt3 = cnt3 + 1
    '''
    This while loop appends the specific amount of # at the end  
    '''

    finalWord = "".join(wrd)                    #finalWord is the wrd array converted to a string
    print(finalWord)                    
    
    
    
    
def main():

    
if __name__ == '__main__':
    main()