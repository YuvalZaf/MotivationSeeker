import smtplib
import datetime  # library that can tell the time and date on your cur location
import random
import os
from twilio.rest import Client


account_sid = "ACd698df8a9b7645ae74d77adebf0798c0"  # account on twilo web
auth_token = "6dfdd300e306de1251808547a8b52826"  # id for twilio web(needs to me env var)
client = Client(account_sid, auth_token)

EMAIL = "yuvalz528@gmail.com"
PASSWORD = "lrulnfeuclepdhor"

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
                from_="+18658004107",
                to='+972523948372'
            )
            print(message.status)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs="yuvalz528@gmail.com",
                                msg=f"subject: Motivation for the week\n\n {mail}")


