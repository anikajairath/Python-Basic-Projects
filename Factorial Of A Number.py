def fact(n):
    
    if n==0 or n==1: #Base Case
        return 1
    
    else:
        return n * fact(n-1)
    
n = int(input("Enter a number for factorial: "))
fact(n)

print(f"The factorial of {n} = {fact(n)}")
