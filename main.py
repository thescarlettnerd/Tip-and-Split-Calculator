print("Welcome to the Tip and Split Calculator!")
bill_total = input("What was the total bill? $")
tip_percent = input("What percent would you like to tip? ")
peeps = input("How many people are splitting the bill? ")

tip = float(tip_percent) / 100 + 1
split_bill = float(bill_total) / float(peeps)

bill_each = float(split_bill) * float(tip)

result = round(bill_each, 2)

print(f"Each person should pay ${result}")