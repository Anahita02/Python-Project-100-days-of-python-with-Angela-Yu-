# with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\002 weather-data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv

# with open(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\002 weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)

#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv(r"C:\Users\Home\Desktop\Python Project (100 days of python with Angela Yu)\Python-Project-100-days-of-python-with-Angela-Yu-\002 weather-data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)

# average_temp = data["temp"].mean()
# print(average_temp)

# max_temp = data["temp"].max()
# print(max_temp)


# # Get data in columns

# # print(data["condition"])
# print(data.condition)


# Get data in rows
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp_in_fahrenheit = monday.temp * 9/5 + 32
# print(monday_temp_in_fahrenheit)

# Crete a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)