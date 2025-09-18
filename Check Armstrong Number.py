def isArmstrong(num): # A function that takes a number.
    
    orig = num   # Keeping a copy to compare at the end.
    
    d = len(str(num))  # Number of digits (e.g. for 153, length = 3).
    
    total = 0  # This will accumulate digit**d for each digit.
    
    while num > 0:  # Process digits from right to left until num becomes 0.
        
        digit = num % 10  # Get the last digit.
        total = total + digit**d  # Add digit raised to the power of number of digits.
        num = num // 10  # Drop the last digit.
        
    if total == orig:  # After the loop, compare the sum with the original number.
        print(f"{orig} is an Armstrong Number")
    else:
        print(f"{orig} is not an Armstrong Number")


num = int(input("Enter A Number: ")) 
isArmstrong(num)                     


