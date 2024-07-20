#challenge4

age= input ("What is your current age?")
age_int= int(age)
years_remaning= 90 - age_int
days_remaning=years_remaning*365
weeks_remaning=years_remaning*52
months_remaning=years_remaning*12
message=f"You have {days_remaning} days, {weeks_remaning} weeks and {months_remaning} months left."
print(message)