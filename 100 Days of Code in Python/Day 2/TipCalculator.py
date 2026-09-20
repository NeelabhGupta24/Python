print("Welcome to the tip calculator")
bill = float(input("What was your bill ? $"))
tip = float(input("How much tip would you like to give ? %"))
people = int(input("How many people  are splitting the bll? "))
amount =  bill*((tip/100)+1)/people # calculating amount each person has to pay
print(f"Each person has to pay ${round(amount,2)}")