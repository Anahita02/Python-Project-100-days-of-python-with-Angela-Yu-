from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    # pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entery.get()
    email_username = email_username_entry.get()
    password = password_entry.get()   

    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Not valid", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail: {email_username} \nPassword: {password} \nIs it ok to save?") 

        if is_ok:
            try:
                with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day30\data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day30\data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)

                with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day30\data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entery.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entery.get()
    try:
        with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day30\data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Not Found", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Result", message=f"The website name is {website} \n The Email/Username is {email} \nThe password is {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
my_pass_image = PhotoImage(file=r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day29\logo.png")
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(row=0, column=1)

# Labels 
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Enteries
website_entery = Entry(width=16)
website_entery.grid(row=1, column=1)
website_entery.focus()

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "anna@gmail.com")

password_entry = Entry(width=16)
password_entry.grid(row=3, column=1)

# Butttons
search_button = Button(text="Search", width=15 ,command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()