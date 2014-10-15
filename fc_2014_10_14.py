#!/usr/bin/env python
#imports go here
import datetime
import smtplib

from email.mime.text import MIMEText

from github import Github

#
# Free Coding session for 2014-10-14
# Written by Matt Warren
#
hub = Github()

hub_user = hub.get_user('mfwarren')

event = hub_user.get_public_events()[0]  # the most recent public event

last_event_time = event.created_at
last_event_time = last_event_time + datetime.timedelta(hours=-6) # GMT To Mountain Time

if last_event_time.day != datetime.date.today().day:
    msg = MIMEText("You haven't made any commits to GitHub yet today!")
    msg['Subject'] = "GITHUB ALERT!"
    msg['From'] = 'me@example.com'
    msg['To'] = 'me@example.com'
    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()
