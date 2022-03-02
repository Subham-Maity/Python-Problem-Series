"""Python:Same as Java, we’re using Case switch method here, “match-case”.Python 3.10 (2021) introduced the match-case statement which provides a first-class implementation of a "switch" for Python."""
x = int(input("Please enter the no. of your month: \n"))
 
sentence = "The name of the month according to your number is:"
match x:
    case 1:
        print(f"{sentence} January")
    case 2:
        print(f"{sentence} February")
    case 3:
        print(f"{sentence} March")
    case 4:
        print(f"{sentence} April")
    case 5:
        print(f"{sentence} May")
    case 6:
        print(f"{sentence} June")
    case 7:
        print(f"{sentence} July")
    case 8:
        print(f"{sentence} August")
    case 9:
        print(f"{sentence} September")
    case 10:
        print(f"{sentence} October")
    case 11:
        print(f"{sentence} November")
    case 12:
        print(f"{sentence} December")  
