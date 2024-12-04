def swap_dec(fn): # division(2,10)

    def wrapper(n1,n2): #n1=2,n2=10
      
        if n1<n2: #2>10
           
           (n1,n2)=(n2,n1) # n1=10,n2=2
    
        return fn(n1,n2)
    
    return wrapper

def swap_round(fn):

    def wrapper(num1,num2):

        num1=round(num1)

        num2=round(num2)

        return fn(num1,num2)
    
    return wrapper


@swap_round
@swap_dec
def add_numbers(num1,num2):
    
    return num1+num2

@swap_round
@swap_dec
def substraction(num1,num2):

    return num1-num2

@swap_round
@swap_dec
def division(num1,num2):

    return num1/num2 

print(substraction(3.6,7.6))