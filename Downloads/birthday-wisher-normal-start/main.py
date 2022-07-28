# #################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

# ##############--------- Check if today matches a birthday in the birthdays.csv-------#####################
date = dt.datetime.now()
today = (date.month, date.day)
my_email = "testerudemy1@gmail.com"
password = "tnggovmzeydoemao"

print(today)

birthday_data = pandas.read_csv("/Users/HP/Downloads/birthday-wisher-normal-start/birthdays.csv")
birthdays_dict = {(birthday_data_row["month"], birthday_data_row["day"]): birthday_data_row
                  for (index, birthday_data_row) in birthday_data.iterrows()}

if today in birthdays_dict:
    file_path = (f"/Users/HP/Downloads/birthday-wisher-normal-start/"
                 f"letter_templates/letter_{random.randint(1,3)}.txt")
    birthday_person = birthdays_dict[today]
    with open(file_path) as birthday_letters_file:
        birthday_letter = birthday_letters_file.read()
        new_birthday_letter = birthday_letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{new_birthday_letter}")






