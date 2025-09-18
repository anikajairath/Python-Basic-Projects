#Importing the library
import re

#Opening the file in read mode by sharing the file address
fhand = open("C:/Users/admin/Desktop/Python Progs/Data.txt", "r")

#A variable to store the total sum, initialised to 0
tot_sum = 0;

for line in fhand:
    
    #To strip all the whitespaces from the line
    line = line.strip()
    
    #Creating a list 'numbers' to store numerical values from each line, using a regex expression with findall()
    numbers = re.findall('[0-9]+', line)
    
    #If numerical values found and 'numbers' is not an empty list
    if len(numbers) > 0:
    
        for num in numbers:
            
            #Convert each numerical string to integer using int() method
            num = int(num)
            
            #Add each one to total sum
            tot_sum = tot_sum + num

#Close file        
fhand.close()

#Print the sum
print("The Sum is", tot_sum)