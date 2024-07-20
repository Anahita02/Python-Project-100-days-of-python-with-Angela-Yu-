#final project

from random import choice


print("Welcome to Teasure iland.\nYour mission is to find the treasure.")

choice1= input("You're at a crossroad, where do you want to go? Type 'left' or 'right'. \n").lower()


if choice1 == "left":
    choice2 = input("You've come to a lake. There is am island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if choice2 == "wait":
       choice3 = input("You arrive at the island ynharmed. There i s house with 3 doors. One red, one yellow and one blue. which color do you choose? \n").lower()
       if choice3 == "red":
          print("It's a room full of fire. Game Over.")
       elif choice3 == "yellow":
           print("You found the treasure! You Win!")
       elif choice3 == "blue":
           print("You enter a room of beasts. Game Over.") 
    else:
       print("You got attack by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")