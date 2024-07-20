#challenge3

height = float(input("Enter your height in m: "))
weight = float(input("Enter your wieght in kg: "))

BMI = int(weight) / float(height) ** 2


if BMI < 18.5:
    print(f"You BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"You BMI is {BMI}, you are normal weight.")
elif BMI < 30:
   print(f"You BMI is {BMI}, you are over weight.")
elif BMI < 35:
    print(f"You BMI is {BMI}, you are obese.")
else:
    print(f"You BMI is {BMI}, you are clinnically obese.")