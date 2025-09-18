n = int(input("\nEnter Ending Range For The Sequence: "))

sumofsq = 0

for x in range(1, n+1):
    sumofsq = sumofsq + x*x
    
print(f"\nThe sum of squares of series till {n} = {sumofsq}")
    