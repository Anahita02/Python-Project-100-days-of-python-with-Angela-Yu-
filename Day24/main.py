file = open("C:/Users/Home/Desktop/Python Project (100 days of python with Angela Yu)/Python-Project-100-days-of-python-with-Angela-Yu-/Day24/my_file.txt")
contents = file.read()
print(contents)

file.close()


# if you are going to forget the close method you better use this form

with open("C:/Users/Home/Desktop/Python Project (100 days of python with Angela Yu)/Python-Project-100-days-of-python-with-Angela-Yu-/Day24/my_file.txt") as file:
    contents = file.read()
    print(contents)

# How to wirte in a file?
with open("C:/Users/Home/Desktop/Python Project (100 days of python with Angela Yu)/Python-Project-100-days-of-python-with-Angela-Yu-/Day24/my_file.txt", mode="w") as file:
    # It delets every thing in tmy_file and write 'New text.'
    file.write("New text.")


# If you want to have all the things in the file but you want to add something in it you should change the mode to a wich stands for append
with open("C:/Users/Home/Desktop/Python Project (100 days of python with Angela Yu)/Python-Project-100-days-of-python-with-Angela-Yu-/Day24/my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# If you try to open a file in write mode and that file doesn't exist, then it's going to actually create it for you from scratch.
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")