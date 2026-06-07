# FileNotFound
with open("a_file.txt") as file:
    file.read()

# FileNotFound Exception
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["saadasda"])
except FileNotFoundError:
    # print("There was an error")

    # Create it if there is not 
    file = open("a_file.txt", "w")
    file.write("Someting")

except KeyError as error_message:
    print(f"The key {error_message} does not exit.")

else:
    content = file.read()
    print(content)

finally:
    # file.close()
    # print("File was closed.")

    # raise KeyError

    # raise TypeError
    raise TypeError("This is an error that I made up.")

# KeyError
a_dictionary = {"key": "value"}
value = a_dictionary["non_existent_key"]

# InddexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

#TypeError
text = "abc"
print(text + 5)

