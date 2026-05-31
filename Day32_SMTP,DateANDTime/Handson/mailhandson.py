import smtplib
import os
my_email = "pysuclearning@gmail.com"
my_password = "tqbf tzmg assk cbjn"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# #tls- transport layer security - which encrypts the mail
# connection.login(user=my_email, password=password)
# connection.sendmail(my_email,
#                     "rupapaineni@gmail.com",
#                     msg = "Hello\n\nThis is a test email from Python.")
# connection.close()

#if we want to send mail similar to file inorder to skip connection.close() line

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    # tls- transport layer security - which encrypts the mail
    connection.login(user=my_email, password=my_password)
    connection.sendmail(my_email,
                        "pysuclearning@gmail.com",
                        msg="Hello\n\nThis is a test email from Python.")