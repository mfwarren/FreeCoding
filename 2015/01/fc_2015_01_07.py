#!/usr/bin/env python3
# imports go here
import os
import gspread
import datetime
import argparse

from oauth2client.client import OAuth2WebServerFlow
from oauth2client import tools
from oauth2client.file import Storage

#
# Free Coding session for 2015-01-07
# Written by Matt Warren
#


CLIENT_ID = os.envget('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.envget('GOOGLE_CLIENT_SECRET')


storage = Storage('creds.data')
credentials = storage.get()

if credentials.invalid:
    flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               scope='https://spreadsheets.google.com/feeds https://docs.google.com/feeds',
                               redirect_uri='http://localhost')
    parser = argparse.ArgumentParser(parents=[tools.argparser])
    flags = parser.parse_args()

    credentials = tools.run_flow(flow, storage, flags)

gc = gspread.authorize(credentials)

spreadsheet = gc.open("Books")
books = spreadsheet.sheet1.get_all_values()

# convert to list of dictionaries using first row as keys
books = [{books[0][i]: book[i] for i in range(len(books[0]))} for book in books[1:]]

ten_days_ago = datetime.datetime.now() + datetime.timedelta(days=-10)

recent_book = None
for book in books:
    d = datetime.datetime.strptime(book['Finished'], '%d/%m/%Y')
    if d > ten_days_ago:
        recent_book = book
        break

if recent_book is None:
    print("YOU SUCK -  GO READ SOMETHING")
else:
    print("YOU FINISHED %s on %s" % (recent_book['Title'], recent_book['Finished']))
