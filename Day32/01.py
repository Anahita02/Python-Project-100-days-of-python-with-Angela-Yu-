import smtplib


my_email = "appbreweryinfo147@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
# connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password="password")
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="appbreweytesting@yahoo.com", 
        msg="Subject:Hello\n\nThis is the body of my email")

# connection.close()







import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))

year = now.year
print(year)
print(type(year))

if year == 2026:
    print("Wear a face mask")


month = now.month
print(month)

day_of_week = now.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)