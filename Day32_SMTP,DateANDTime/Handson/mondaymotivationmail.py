import random
import smtplib
import datetime

my_email = "pysuclearning@gmail.com"
password = "godn airl elwg znuj"

today = datetime.datetime.now()
if today.weekday()==2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        # tls- transport layer security - which encrypts the mail
        connection.login(user=my_email, password=password)
        connection.sendmail(my_email,
                            "chandupraveeng@gmail.com",
                            msg=f"Subject:Monday Motivation \n\n {quote}")







