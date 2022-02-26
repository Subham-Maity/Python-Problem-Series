sub1 = int(input("Enter the number of your Subject 1 (Physics) : "))
sub2 = int(input("Enter the number of your Subject 2 (Math) : "))
sub3 = int(input("Enter the number of your Subject 3 (Biology) : "))
 
total = sub1+sub2+sub3
print("Total marks :", total, "out of 300")
print("Your CGPA is", total/30)