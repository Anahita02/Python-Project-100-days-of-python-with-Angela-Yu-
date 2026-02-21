# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.



import pandas as pd

df  = pd.read_csv(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\Day26\nato_phonetic_alphabet.csv")

dic = {row.letter: row.code for (index, row) in df.iterrows()}

user_words = input("Enter a word: ").upper()

Nato = [dic[letter] for letter in user_words]

print(Nato)
