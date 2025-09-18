def isArmstrong(num):          # Define a function that takes a number.
    
    orig = num                 # Keep a copy to compare at the end (because we'll change num).
    
    d = len(str(num))          # Number of digits (e.g., 153 -> "153" -> length 3).
    
    total = 0                  # This will accumulate digit**d for each digit.
    
    while num > 0:             # Process digits from right to left until num becomes 0.
        
        digit = num % 10       # Get the last digit. (e.g., 153 % 10 -> 3)
        total = total + digit**d  # Add digit raised to the power of number of digits.
        num = num // 10        # Drop the last digit. (e.g., 153 // 10 -> 15)
        
    if total == orig:          # After the loop, compare the sum with the original number.
        print(f"{orig} is an Armstrong Number")
    else:
        print(f"{orig} is not an Armstrong Number")


num = int(input("Enter A Number: "))  # Read input as an integer.
isArmstrong(num)                      # Call the function.

