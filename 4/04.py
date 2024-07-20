#challenga4

import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

if not names:
    print("No names provided. Please enter at least one name.")
else:
    random_num = random.randint(0,len(names)-1)
    print(f"{names[random_num]} is going to buy the meal today!")
