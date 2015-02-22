#!/usr/bin/env python3
# imports go here
from icalendar import Calendar, Event
from datetime import datetime
import pytz

#
# Free Coding session for 2015-02-21
# Written by Matt Warren
#

cal = Calendar()

# required iCal properties:
cal.add('prodid', '-//Matt Warren Calendar//mxm.dk//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Read a book')
event.add('dtstart', datetime(2015, 2, 28, 8, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2015, 2, 28, 9, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2015, 2, 28, 9, 0, 0, tzinfo=pytz.utc))

cal.add_component(event)

with open('book.ics', 'wb') as f:
    f.write(cal.to_ical())
