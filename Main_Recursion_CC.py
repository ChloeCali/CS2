'''
Created on Nov 8, 2022

@author: CCaliboso24
'''

def get_factorial(n):                                               # Factorial of a number using recursion
    if n == 1:
       return n                                                     #The number is 1
    else:
       return n*(get_factorial(n-1))                                #Runs several loops and does math equations to find the factorial of any given number

def get_summation(n):
    if n> 0:
        n = n + get_summation(n-1)                                  #this line adds the given number to every single number subtracted 1 recursively
        return n
    elif n == 0:                                         
        n = 0                                                       #The number is 0
        return n                                                    #Returns the summed number

def get_powers(a,n):
    if n> 0:
        n = a * get_powers(a,n-1)                                   #This codes the first given number to the power of the second given number
        return n
    elif n == 0:
        n = 1                                                       #The number is 1
        return n                                                    #Returns the number

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

def get_compound_interest_balance(balance, rate, time):
### function calculates the compound interest of a balance based on three inputs
### inputs: balance (starting balance); rate (interest rate); time (time in years)
### output: new value of balance with interest

    if time == 0:                                                                   # bool, if zero years pass, the balance gains no interest
        return balance                                                              # float, ex: '100', when balance gains no interest, function returns original value

    if time > 0:                                                                    # bool, if time is greater than 0, balance gains interest each year
        return get_compound_interest_balance(balance * rate, rate, time - 1)        # new inputs, ex: '110, 1.1, 0', calculates new balance, keeps rate constant, subtracts one from time


def get_GCD(x,y):
    
### functions gets the greatest common denominator of two ints with conditions above
### inputs: x & y (both ints)
### output: greatest common denominator of x & y (also an int)
    
    if y <= x and (x % y) == 0:                                                     # bool, conditions for GCD
        return y                                                                    # int, ex: '2', returns y value

    else:                                                                           # bool, if inputs do not meet conditions in if statement
        def get_Euclids_Algorithm(x,y):
        ### functions gets the greatest common denominator of two ints with conditions above
        ### inputs: x & y (both ints)
        ### output: greatest common denominator of x & y (also an int)
            get_GCD(y, x % y)                                                       # calls get_GCD() function

def get_compound_interest_balance(balance,rate,time):
    
### function calculates the compound interest of a balance based on three inputs
### inputs: balance (starting balance); rate (interest rate); time (time in years)
### output: new value of balance with interest

    if time == 0:                                                                   # bool, if zero years pass, the balance gains no interest
        return balance                                                              # float, ex: '100', when balance gains no interest, function returns original value
    elif time > 0:                                                                  # bool, if time is greater than 0, balance gains interest each year
        return get_compound_interest_balance(balance * rate, rate, time - 1)        # new inputs, ex: '110, 1.1, 0', calculates new balance, keeps rate constant, subtracts one from time
    
def get_product_of_2_whole_numbers(a,b):
    
### function gets the product of two whole numbers
### inputs: a & b (two ints)
### output: one int (the product of a * b)
    if b == 0:                                                                      # bool, when b is zero, the product is zero
        return 0                                                                    # int, '0'

    if b > 0:                                                                       # bool, when b greater than zero, finds product of two ints
        return a + get_product_of_2_whole_numbers(a, b - 1)                         # int, ex: '6', finds product of a * b


def main():     

    
    start1 = ("select a function number:\n1. factorial\n2. summation\n3. powers\n4. sum of a number's digits\n")        # variable - first part of input textused to combine later
    start2 = ("5. fibonacci\n6. GCD\n7. compound interest balance\n8. product of 2 whole numbers\n")                    # variable - first part of input textused to combine later
    
    ask1 = input(start1 + start2)                                                   #input - asks user to choose function to call 
    
    if ask1 == "1":                                                                 # conditional - if ask1 == 1, call for factorial function 
        ask2 = input("insert input number\n")                                       # input - asks user for number that will be used in the factorial function parameter
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        print(get_factorial(ask2))                                                  # calls factorial function and prints result
        
    elif ask1 == "2":                                                               # conditional - if ask1 == 2, call for the summation function
        ask2 = input("insert input number\n")                                       # input - asks user for number that will be used in the summation function parameter
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int        
        print(get_summation(ask2))                                                  # calls summation function and prints result 
        
    elif ask1 == "3":                                                               # conditional - if ask1 == 3, call for powers function
        ask2 = input("insert input base\n")                                         # input - asks user for base of the exponent
        ask3 = input("insert input power\n")                                        # input - asks user for the power of the exponent
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        ask3 = int(ask3)                                                            # variable - converts ask3 from str to int
        print(get_powers(ask2,ask3))                                                # calls powers function and prints result
        
    elif ask1 == "4":                                                               # conditional - if ask1 == 4, call for sum of a number's digits function
        ask2 = input("insert input number\n")                                       # input - asks user for number that will be used in the facotrial function parameter                        
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        print(get_sum_of_numers_digits(ask2))                                       # calls sum of a number's digits function and prints result
         
    elif ask1 == "5":                                                               # conditional - if ask1 == 5, call for fibonacci function
        ask2 = input("insert input number\n")                                       # input - asks user for number that will be used in the fibonnaci function parameter
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        print(get_fibonacci(ask2))                                                  # calls fibonacci function and prints result
        
    elif ask1 == "6":                                                               # conditional - if ask1 == 6, call for fibonacci function
        ask2 = input("insert input first number\n")                                 # input - asks user for balance for the compound interest balance function
        ask3 = input("insert input second number\n")                                # input - asks user for balance for the compound interest balance function
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        ask3 = int(ask3)                                                            # variable - converts ask3 from str to int
        print(get_GCD(ask2,ask3))
        
    elif ask1 == "7":                                                               # conditional - if ask1 == 7, call for fibonacci function
        ask2 = input("insert input balance\n")                                      # input - asks user for balance for the compound interest balance function
        ask3 = input("insert input rate\n")                                         # input - asks user for rate for the compound interest balance function
        ask4 = input("insert input time\n")                                         # input - asks user for time for the compound interest balance function
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        ask3 = int(ask3)                                                            # variable - converts ask3 from str to int
        ask4 = int(ask4)                                                            # variable - converts ask4 from str to int
        print(get_compound_interest_balance(ask2,ask3,ask4))                        # calls compound interest balance function and prints result
        
    elif ask1 == "8":                                                               # conditional - if ask1 == 8, call for product of 2 whole numbers 
        ask2 = input("insert input first number\n")                                 # input - asks user for first multiple for the product of 2 whole numbers functions
        ask3 = input("insert input second number\n")                                # input - asks user for second multiple for the product of 2 whole numbers functions
        ask2 = int(ask2)                                                            # variable - converts ask2 from str to int
        ask3 = int(ask3)                                                            # variable - converts ask3 from str to int
        print(get_product_of_2_whole_numbers(ask2,ask3))                            # calls product of 2 whole numbers and prints result
        
    else:
        main()
    
    
        
        
        
        
        
        
    
if __name__ == "__main__":
    main()  