
"""So here we did like this
 
Take a number from the user and compare them using < / > and store it in the boolean data type because if you compare two operators it returns true or false"""


given_number = 56
print("The given number is", given_number)
 
user_input = int(input("Enter your number : \n"))
 
if user_input < given_number:
    print("Given number is greater than the entered number")
elif user_input == given_number:
    print("Both are same number")
else:
    print("Given number", given_number, "is less than the entered number")
