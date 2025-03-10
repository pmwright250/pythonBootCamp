print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = 1.0 + (tip / 100)
total_per_person = (bill / people) * tip
print(f"Each person should pay: ${round(total_per_person,2)}")