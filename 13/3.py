year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leep year.")
        else:
            print(" Not leep year.")
    else:
        print("Leep year.")
else:
    print("Not leap year.")