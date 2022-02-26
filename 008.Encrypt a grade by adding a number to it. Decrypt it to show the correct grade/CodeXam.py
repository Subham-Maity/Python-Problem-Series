""" 
Python : To install “Click” package simply go to any terminal and type “pip install click”
 
1. We used 'Click' module by this command "import click"
2. Take a input as a string for your grade
3. Take a input as an string for your code
4. use 'click' for take yes or no on input
       
Python click module is used to create command-line (CLI) applications.
It is an easy-to-use alternative to the standard optparse and argparse modules."""
import click
 
result = input("Please Enter Your Exam Grade: ")
code = input("Please Enter Your Encryption Code: ")
 
print("\nNow Your Grade is 'F'")
 
if click.confirm("\nSir/Ma'am, Do You Want to Decrypt Your Grade ? If Yes type 'Y/y' or 'N/n' for No :\n>> ",
                 default=True):
    print("Your Actual Grade is ", result)
else:
    print("Grade Decryption Aborted")
