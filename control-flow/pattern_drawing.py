size = int(input("Enter the size of the pattern, Must be a number: "))

row = 0

while True :
   
    while row < size:
    
        for col in range(size):
            print("*", end="")  
        print()  
        row += 1