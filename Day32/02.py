import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "appbreweryinfo147@gmail.com"

if day_of_week == 0:
    with open("quotes.txt") as quote_file:
        quotes = random.choice(quote_file.readlines())
    print(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="password")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="appbreweytesting@yahoo.com",
            msg=f"Subject:motivation quote\n\n{quotes}"
        )
        
