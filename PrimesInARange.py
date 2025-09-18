def genprimes(x, y):
    
    primelist = [] #declaring an empty list
    
    for n in range(x, y+1):
        
        if n < 2:
            continue
        
        isPrime = True
        
        for t in range(2, n-1):
            
            if n%t == 0:
                isPrime = False
                break
                
        if isPrime is True:
            primelist.append(n)
    
    print(f"\nThe Primes in the range of {x} and {y} are: {primelist}")

start_range = int(input("\nEnter The Starting Range: "))
end_range = int(input("\nEnter The Ending Range: "))

genprimes(start_range, end_range)