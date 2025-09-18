num = 0
tot = 0.0

while True:
    sval = input("Enter A Number: ")
    
    if sval == "Done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Data")
        continue
    
    num = num + 1
    tot = tot + fval
        
print(tot, num, tot/num)