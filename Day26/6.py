student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)


# Looping through Pandas DataFrame
import pandas as pd

student_df = pd.DataFrame(student_dict)

# print(student_df)

# for (key, value) in student_df.items():
#     # print(key)
#     print(value)

for (index, row) in student_df.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)