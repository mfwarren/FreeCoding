#!/usr/bin/env python3
# imports go here
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#
# Free Coding session for 2015-04-27
# Written by Matt Warren
#


def send_email(from_email, to_emails):
    msg = MIMEMultipart()
    msg['Subject'] = 'Weekly KPI Report'
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg.preamble = "Here's the weekly KPI Report"

    with open('report.png', 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)

    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

if __name__ == '__main__':
    send_email('matt.warren@gmail.com', ['matt.warren@gmail.com'])
