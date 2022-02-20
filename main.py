##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today_tuple = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")

wedding_day_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in wedding_day_dict:
    wedding_day_couple = wedding_day_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as data_file:
        content = data_file.read()
        content = content.replace("[NAME]", wedding_day_couple['name'])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection :
            connection.starttls()
            connection.login("youremail@gmail.com", "TestMeUpNow")
            connection.sendmail(
                from_addr="youremail@gmail.com",
                to_addrs=wedding_day_couple['email'],
                msg=f"Subject:Happy Wedding anniversary\n\n{content}"
            )

