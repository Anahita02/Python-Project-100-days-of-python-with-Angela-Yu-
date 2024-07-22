#final project

from art import logo, vs
from game_data import data
import random
from replit import clear

def frormat_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_ans(guess, a_fllowers, b_followers):
    """Takes the user guess and and follower counts and returns if they got it right."""
    if a_fllowers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#art
print(logo)

score = 0
should_continue = True
#random person
b_account = random.choice(data)

while should_continue:
    #Making account at position B become the nex account at possition A.    
    a_account = b_account
    b_account = random.choice(data)
    if a_account == b_account:
        b_account = random.choice(data)

    print(f"You're right! Current score: {score}")
    print(f"Compare A: {frormat_data(a_account)}")
    print(vs)
    print(f"Against B: {frormat_data(b_account)}")

    #user guess
    guess = input("who hase more followers? Type 'A' or 'B': ").lower()

    #check user ans
    a_follower_count = a_account["follower_count"]
    b_follower_count = b_account["follower_count"]

    is_correct = check_ans(guess, a_follower_count, b_follower_count)

    #clear
    clear()

    print(logo)
    
    #give feed back on the guses.
    if is_correct:
        score +=1 
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry that's wrong. Finall score: {score}.")
        should_continue = False

