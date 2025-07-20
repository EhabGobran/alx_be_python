user_input = int(input("Enter the size of the pattern: "))
for i in range(1,user_input+1):
    if i != 1:
        print()
    for j in range(1,user_input+1):
        print('*',end="")