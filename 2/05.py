#final project

print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
bill_float= float(bill)
percentage=input("what percentage tip would you like to give? 10, 12 or 15? ")
percentage_float= float(percentage)
people=input("How many people tp split the bill? ")
people_int=int(people)
tip= bill_float*(percentage_float/100) 
pay = round((bill_float+ tip)/people_int , 2) 
print(f"Each person should pay: ${pay}")