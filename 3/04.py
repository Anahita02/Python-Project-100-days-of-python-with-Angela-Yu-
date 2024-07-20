#challenge 4

year = int(input("Which year do you want to check? "))

if year % 4 ==0:
    print("It is a Leap year.")
    if year % 100==0:
      print ("It is a Leap year.")
      if year % 400==0:
        print ("It is a Leap year.")
      else:
        print("It is not a Leap year.")
    else:
       print("It is not a Leap year.")
else:
    print("It is not a Leap year.")