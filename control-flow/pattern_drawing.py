user_input = int(input("Enter the size of the pattern, Must be a number: "))

row = 0
   
while row < user_input :

    for col in range(user_input):
        print("*", end="")  
    print()  
    row += 1