"""So here we did like this
         
        avg = (subject1 + subject2 + subject3)/3.0
        If Conditions: avg>=40 && subject1>=33 && subject2>=33 && subject3>=33
           print"Congratulations, You have been promoted"
        Else print"Sorry, You have not been promoted! Please try again."""



physics = int(input("Enter your score in Physics:\n"))
chemistry = int(input("Enter your score in Chemistry:\n"))
mathematics = int(input("Enter your score in Mathematics:"))
 
result = (physics+chemistry+mathematics) / 3
print("\nYour overall percentage is", result)
if result >= 40 and physics >= 33 and chemistry >= 33 and mathematics >= 33:
    print("Congratulations ! You've been promoted ")
else:
    print("Ah , You've failed this year ! See you never :)")
