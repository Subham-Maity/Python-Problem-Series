"""Python : We will use the .replace() method again and unlike java , we don’t need to store the string in another variable !"""
name = input("Enter your name: ")
 
output = "Dear <|Name|>, Thanks a Lot !"
 
print(output.replace('<|Name|>', name))