"""Python : 
1st approach = Just same as Java approach mentioned above
 
2nd Approach = In python we can simply use pip(package manager)  to install a python package which is called “sympy” , just go to your terminal(for windows CMD or Powershell or Windows Terminal for Win 11, system terminal for MaxOS and any Linux Based OS) and type “pip install sympy”, it will automatically download and install sympy. After that, type “from sympy import *” on your IDE (see the 1st line of the python solution mentioned below). Then we can use the isprime() method which we imported from sympy !
 
P.S. To uninstall any kinda pip package just type “pip uninstall package_name”
"""
num = int(input("Enter Your Number :\n"))
if num > 1:
 
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")
 
 
#2nd approach
from sympy import *
 
x = int(input("Enter a number to check whether it's a Prime number or not:\n"))
 
if isprime(x):
    print(x, "is a prime number indeed")
else:
    print(x, "is not a prime number")

