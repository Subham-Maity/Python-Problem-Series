 
maximum_numbers = int(input("Enter The Maximum Marks of One Subject (example: Physics 100) : "))
 
physics = int(input("Enter the number of your Subject 1 (Physics) : "))
 
math = int(input("Enter the number of your Subject 2 (Math) : "))
 
biology = int(input("Enter the number of your Subject 3 (Biology) : "))
 
chemistry = int(input("Enter the number of your Subject 4 (Chemistry) : "))
 
optional = int(input("Enter the number of your Subject 5 (Optional) : "))
 
 
total_marks = physics + math + biology + chemistry + optional
max_possible_marks = (maximum_numbers*5)
 
print("Total marks : ", total_marks)
print("Percentage of your 5 Subject is: ", (total_marks/max_possible_marks)*100)