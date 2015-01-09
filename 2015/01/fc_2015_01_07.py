#!/usr/bin/env python3
# imports go here
import os
import gspread
import datetime
import argparse

from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools
from oauth2client.file import Storage


import smtplib
from email.mime.text import MIMEText

#
# Free Coding session for 2015-01-07
# Written by Matt Warren
#


GMAIL_LOGIN = os.getenv("EMAIL_USERNAME")
GMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

ten_days_ago = datetime.datetime.now() + datetime.timedelta(days=-10)


def get_credentials():
    storage = Storage('creds.data')
    credentials = storage.get()

    if credentials is None or credentials.invalid:
        flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   scope='https://spreadsheets.google.com/feeds https://docs.google.com/feeds',
                                   redirect_uri='http://localhost')
        parser = argparse.ArgumentParser(parents=[tools.argparser])
        flags = parser.parse_args()

        credentials = tools.run_flow(flow, storage, flags)

    return credentials


def read_spreadsheet(name="Books"):
    gc = gspread.authorize(get_credentials())

    spreadsheet = gc.open(name)
    books = spreadsheet.sheet1.get_all_values()

    # convert to list of dictionaries using first row as keys
    books = [{books[0][i]: book[i] for i in range(len(books[0]))} for book in books[1:]]
    return books


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


def main():
    recent_book = None
    for book in read_spreadsheet():
        d = datetime.datetime.strptime(book['Finished'], '%d/%m/%Y')
        if d > ten_days_ago:
            recent_book = book
            break

    if recent_book is None:
        send_email("[Nag] Read A Book!", "You need to update the spreadsheet with another book.")


if __name__ == "__main__":
    main()
