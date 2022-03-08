"""Python : Simple use of if, elif, else methods"""
print("""         Income Slab                Tax
         ============                ====
         2.5L –  5.0L                5%
         5.0L – 10.0L                20%
         Above  10.0L                30%
* Note that there is no tax for income below or equal to 2.5L *""")
 
income = int(input("\nEnter your annual income:\n"))
 
tax1 = (5/100)
tax2 = (20/100)
tax3 = (30/100)
sentence = "Your annual tax is"
 
if income <= 250000:
    print("You have no annual Tax charge !")
elif 250000 < income <= 500000:
    tax = ((income-250000)*tax1)
elif 500000 < income <= 1000000:
    tax = ((500000-250000) * tax1 + (income - 500000)*tax2)
else:
    tax = ((500000-250000) * tax1 + (1000000 - 500000)*tax2 + (income - 1000000)*tax3)
 
print(sentence, tax)
