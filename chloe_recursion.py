'''
Created on Nov 8, 2022

@author: CCaliboso24
'''
def get_sum_of_numers_digits(n):                                    #n = parameter, the number which digits will be added
    if n < 10:                                                      #conditional - if n is 1 digit, n = n
        return (n)   
    else:                                                           #conditional - recursively continues to add n%10 to get_sum_of_numers_digits(n/10)
        return (n % 10 + get_sum_of_numers_digits(int(n / 10)))     #converted to int so there's no decimal


def get_fibonacci(n):                                               #n = parameter 
    
    if n == 0:                                                      #conditional - if n == 0 return 0
        return 0    
    elif n == 1:                                                    #conditional - if n == 1 return 1
        return 1    
    elif n > 1:                                                     #conditional - is n is greater than 1, recursively continues to insert the given variable into the fibonacci method
        n = get_fibonacci(n-1) + get_fibonacci(n-2)                 
        return (n)    

