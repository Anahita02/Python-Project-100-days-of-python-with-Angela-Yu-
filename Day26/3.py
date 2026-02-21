file1 = open(r'C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day26\file1.txt', 'r')
file2 = open(r'C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day26\file2.txt', 'r')

file1_contents = file1.readlines()
file2_contents = file2.readlines()

result = [int(num) for num in file1_contents if num in file2_contents]


print(result)