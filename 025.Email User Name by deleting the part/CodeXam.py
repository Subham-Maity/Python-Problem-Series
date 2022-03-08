"""   Python: In python we're simply using slicing, we're printing from index 0 to (index of '@') -1"""
user = input("Please enter your email id:\n")
 
x = user.index("@")
 
user_name = user[0:x]
print("Your username is:", user_name)