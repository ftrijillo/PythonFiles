#!/usr/bin/python3

import smtplib

sender = 'nobody@nobody.com'
receiver = 'ftrijillo68@gmail.com'

message = '''From: From Person <nobody@nobody.com>
To: Frank Trijillo <ftrijillo68@gmail.com>
Subject: This is a test email

This is a test email from Python!
'''

try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.sendmail(sender, receiver, message)
    print("Successfully sent email")
except SMTPException as e:
    print("Error: unable to send email: ", e)