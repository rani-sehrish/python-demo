##################### Extra Hard Starting Project ######################
import os
import pandas
from datetime import datetime
import random
import smtplib
# 1. Update the birthdays.csv
birthday = pandas.read_csv("birthdays.csv")
data = birthday.to_dict( orient="records")
data[0].update({
    "name": "janees",
     "email" : "aispeach1830@gmail.com",
     "year" : 2003,
     "month" :7,
     "day" : 11,
})
new_data = pandas.DataFrame(data)
new_data['year'] = new_data['year'].astype('Int64')
new_data['month'] = new_data['month'].astype('Int64')
new_data['day'] = new_data['day'].astype('Int64')
new_data.to_csv("birthdays.csv",index=False)
address = data[1]["email"]
# 2. Check if today matches a birthday in the birthdays.csv
def check_dates():
    month = birthday["month"][1]
    day = birthday["day"][1]
    now = datetime.now()
    datetime_month = now.month
    datetime_day = now.day
    if month == datetime_month:
        return True
    if day == datetime_day:
        return True
    else:
        return False

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

name = birthday["name"][1]
with open("letter templete/letter_1.txt", "r") as letters:
    letter_1 = letters.read()
with open("letter templete/letter_2.txt", "r") as letters:
    letter_2 = letters.read()
with open("letter templete/letter_3.txt", "r") as letters:
    letter_3 = letters.read()
list_letter = letter_1, letter_2, letter_3
choice_letter = random.choice(list_letter)
if check_dates() == True:
    send_mail = choice_letter.replace("[NAME]", name).replace("Angela", "from Sahrish ❤️")
# 4. Send the letter generated in step 3 to that person's email address.
    my_email = "ranisehrish1830@gmail.com"
    my_password = "qyqqueiqflbuympb"
    my_email = os.environ.get("MY_EMAIL")
    my_password = os.environ.get("MY_PASSWORD")
    massage = f"Subject:Happy Birthday.\n\n{send_mail}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,
        to_addrs=address,
        msg=massage.encode('utf-8'))

else:
    print("no birthday anyone")

