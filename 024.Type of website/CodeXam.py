"""Python : Same like Java, we’re using endswith() method in python as well"""
user_input = input("Please Enter Your URL:\n")
 
if user_input.endswith(".com"):
    print("It's an Commercial Website")
elif user_input.endswith(".org"):
    print("It's an Organization Website")
elif user_input.endswith(".in"):
    print("It's an Indian Website")
else:
    print("Not Found !")