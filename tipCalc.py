print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10%, 12%, 15%? ")) / 100
number_of_people = int(input("How many people to split the bill? "))

amount_per_person = round(((bill * (1 + tip_percentage)) / number_of_people),2)
amount_per_person = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${amount_per_person}")
