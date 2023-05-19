import smtplib
import datetime  # library that can tell the time and date on your cur location
import random
import os
from twilio.rest import Client

account_sid = os.environ.get("twilio_api_sid")  # account on twilo web
auth_token = os.environ.get("twilio_api_token") # id for twilio web(needs to me env var)
client = Client(account_sid, auth_token)

EMAIL = os.environ.get("my_email")
PASSWORD = os.environ.get("password_twilio")


now_time = datetime.datetime.now()  # takes the current time from the comp
now_day = now_time.weekday()  # a num that represents the day number(starts at zero)
print(now_time)

file = open("quotes.txt")
text = file.read()
quotes_data = text.split("\n")


with smtplib.SMTP("smtp.gmail.com") as connection:  # create a new connection to gmail servers
        connection.starttls()  # encrypt the mail message
        connection.login(user=EMAIL, password=PASSWORD)
        if now_day == 6:  # send mails and sms on sundays(counting like in the us, sunday=6)
            mail = random.choice(quotes_data)
            message = client.messages \
                .create(
                body=f"{mail}",
                from_=os.environ.get("twilio_num"),
                to=os.environ.get("my_num")
            )
            print(message.status)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=os.environ.get("my_email"),
                                msg=f"subject: Motivation for the week\n\n {mail}")


