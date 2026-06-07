# import tkinter 

from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
# my_label = tkinter.Label(text="I Aam a label", font=("Arial", 24, "bold"))
my_label = Label(text="I Aam a label", font=("Arial", 24, "bold"))




my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.pack()


# Button

def button_clicked():
    # my_label.config(text="Button got clicked")
    Message = input.get()
    my_label.config(text=Message)


button = Button(text="Click Me", command=button_clicked)
button.pack()



# Entry

input = Entry(width=10)
print(input.get())
input.pack()

window.mainloop()