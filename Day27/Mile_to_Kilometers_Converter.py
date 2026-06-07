from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=1, row=0)

label1 =Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=1, row=1)

label4 =  Label(text="Km")
label4.grid(column=2, row=1)

def Mile_to_Km():
    miles = float(entry.get())
    km = miles * 1.609
    label3.config(text=f"{km}")

button = Button(text="Calculate", command=Mile_to_Km)
button.grid(column=1, row=2)

window.mainloop()