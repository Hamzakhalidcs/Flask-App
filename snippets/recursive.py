"""  
    This is a recursive function to find the factorial of an integer,
    Recursive function means a defined function can call it self until the condition is satisfied """

    
def  factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

num = 8
print("The factorial of the",num, "is", factorial(num))

