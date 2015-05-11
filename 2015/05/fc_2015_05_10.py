#!/usr/bin/env python3
# imports go here
import os
import requests
import smtplib
from email.mime.text import MIMEText

#
# Free Coding session for 2015-05-10
# Written by Matt Warren
#

GMAIL_LOGIN = os.getenv("EMAIL_USERNAME")
GMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SITES = [
    'http://halotis.com',
    'http://mattwarren.co',
    'http://columfurey.com',
    'http://www.routeburn.co',
    'http://persistenceapp.com'
]

def send_email(subject, message, from_addr=GMAIL_LOGIN, to_addr=GMAIL_LOGIN):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(GMAIL_LOGIN, GMAIL_PASSWORD)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.close()

def check_sites(sites):
    for site in sites:
        status = requests.get(site)
        if not status.ok:
            print("{0} is down!".format(site))
            send_email("[Alert] Site down: {0}".format(site),
                       "We've detected that the site {0} is not responding successfully.".format(site))

if __name__ == '__main__':
    check_sites(SITES)
