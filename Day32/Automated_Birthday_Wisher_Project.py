import pandas as pd
import datetime as dt
import random
import smtplib

birthday_data = pd.read_csv(r"Day32\birthdays.csv")
print(birthday_data)

now = dt.datetime.now()
print(now)
month = now.month
day = now.day
my_email = "appbreweryinfo147@gmail.com"

for index, row in birthday_data.iterrows():
    if int(row["month"]) == month and int(row["day"]) == day:
        person_email = row["email"]
        chosen_letter = random.randint(1, 3)
        with open(f"Day32\letter_templates\letter_{chosen_letter}.txt", "r") as letter_file:
            letter_contents = letter_file.read()
            letter_contents = letter_contents.replace("[NAME]", row["name"])
        print(letter_contents)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password="password")
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person_email,
                msg=f"Subject:Happy Birthday\n\n{letter_contents}"
            )
