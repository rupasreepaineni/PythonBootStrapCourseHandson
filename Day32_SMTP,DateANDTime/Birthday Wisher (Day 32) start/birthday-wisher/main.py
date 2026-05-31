##################### Hard Starting Project ######################
import pandas
import datetime
import smtplib
import random

my_email = "pysuclearning@gmail.com"
password = "godn airl elwg znuj"
#STEP1: Get today's month and day
todays_date = datetime.datetime.now() # this will give us the current date and time in the form of a datetime object
today_data =(todays_date.day,todays_date.month)
# 2. Save the data from birthdays.csv into a dictionary.
data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient= "records")
print(birthdays_dict)
# this will give us a list of dictionaries where each dictionary is a row in the csv file

# STEP 3: if fteched csv data is matching then filter the data
match_date = [match for match in birthdays_dict if int(match["day"]) == today_data[0] and int(match["month"]) == today_data[1]]
print(match_date)

# #STEP4: get one random letter and replace name with the actual name from csv file
for person in match_date:
    name = person["name"]
    mail = person["email"]
    selected_files = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    with open(f"letter_templates/{selected_files}") as letter_file:
            letter = letter_file.read()
            new_letter = letter.replace("[NAME]", name)
# STEP5:now we've got the people name, we've to send them the email

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # tls- transport layer security - which encrypts the mail
        connection.login(user=mail, password=password)
        connection.sendmail(my_email,mail,
                            msg=f"Subject:Wishes!!\n\n {new_letter}")
