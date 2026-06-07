# import tkinter 

from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# padding
window.config(padx=100, pady=200)

# Label
# my_label = tkinter.Label(text="I Aam a label", font=("Arial", 24, "bold"))
my_label = Label(text="I Aam a label", font=("Arial", 24, "bold"))




my_label["text"] = "New Text"
my_label.config(text="New Text")

# place
# my_label.place(x=0, y=0)

# grid
my_label.grid(column=0, row=0)

# padidng
my_label.config(padx=50, pady=50)


# Button

def button_clicked():
    # my_label.config(text="Button got clicked")
    Message = input.get()
    my_label.config(text=Message)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)



# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()