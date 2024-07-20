#challenge3

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
BMI = int(weight) / float(height) ** 2
BMI_int = int(BMI)
print(BMI_int)