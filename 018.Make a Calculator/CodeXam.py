"""Python : We take all int value as input and simply use if elif method"""
a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
 
print(f"""
Press 1 : + (Addition): {a} + {b}
Press 2 :  - (Subtraction): {a} - {b}
Press 3 :  * (Multiplication): {a} * {b}
Press 4 :   / (Division): {a} / {b}
Press 5 :  % (Modulo or remainder): {a} % {b}""")
 
user_input = int(input())
 
if user_input == 1:
    print(a+b)
elif user_input == 2:
    print(a-b)
elif user_input == 3:
    print(a*b)
elif user_input == 4:
    print(a / b)
elif user_input == 5:
    print(a % b)
else:
    print("Invalid Input :(") 
