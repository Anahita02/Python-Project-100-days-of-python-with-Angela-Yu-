import pandas as pd

data = pd.read_csv(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\004 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

print(data.columns)

print(data["Primary Fur Color"].value_counts())

new_data_Squirrel = data["Primary Fur Color"].value_counts()
new_data_Squirrel = pd.DataFrame(new_data_Squirrel)
new_data_Squirrel.to_csv("squirrel_count.csv")